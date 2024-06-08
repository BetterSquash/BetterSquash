var videolinks=new Array()

videolinks[0]="https://youtu.be/hTXG-0tugUU";
videolinks[1]="https://youtu.be/4LJjEODRVOY";
videolinks[2]="https://youtu.be/GJGwUq_jAO4";
videolinks[3]="https://youtu.be/QzDdDswBYAI";
videolinks[4]="https://youtu.be/go7GWoSJQxA";
videolinks[5]="https://youtu.be/-1EeNriiRN0";
videolinks[6]="https://youtu.be/j5fuaHMG008";

function RandomVideo(){
window.location=videolinks[Math.floor(Math.random()*videolinks.length)]
}