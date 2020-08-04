from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for
from flask import session

from spotify_requests import spotify

app = Flask(__name__)
app.secret_key = "no"

@app.route("/")
def root():
     return render_template('index.html',
          title="Welcome!")

@app.route("/auth")
def auth():
     return redirect(spotify.AUTH_URL)

@app.route("/callback/")
def callback():

     auth_token = request.args['code']
     auth_header = spotify.authorize(auth_token)
     session['auth_header'] = auth_header

     return(redirect(url_for("profile")))

def valid_token(resp):
     return resp is not None and not 'error' in resp

@app.route('/profile')
def profile():
     if 'auth_header' in session:
          auth_header = session['auth_header']
          profile_data = spotify.get_users_profile(auth_header)

          playlist_data = spotify.get_users_playlists(auth_header)

          recently_played = spotify.get_users_recently_played(auth_header)

          if valid_token(recently_played):
               return render_template('profile.html',
                    user=profile_data,
                    playlists=playlist_data,
                    recently_played=recently_played['items'][:10],
                    title=profile_data['display_name'])
          
          return render_template('profile.html',
                    user=profile_data,
                    title=profile_data['display_name'])
     
     return redirect(url_for('root'))

if __name__ == "__main__":
     app.run(debug=True, port=spotify.PORT)