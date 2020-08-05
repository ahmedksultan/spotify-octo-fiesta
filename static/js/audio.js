var aud0 = document.getElementById("aud0");
var aud1 = document.getElementById("aud1");
var aud2 = document.getElementById("aud2");
var aud3 = document.getElementById("aud3");
var aud4 = document.getElementById("aud4");
var aud5 = document.getElementById("aud5");
var aud6 = document.getElementById("aud6");
var aud7 = document.getElementById("aud7");

function playAudio(item) {
     item.play();
     console.log("Playing");
}

function stopAudio(item) {
     item.pause();
     item.currentTime = 0;
     console.log("Stopping")
}