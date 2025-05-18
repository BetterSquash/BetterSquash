var questionlinks=new Array()

questionlinks[0]="../questions/does-the-ball-have-to-bounce-in-squash.html";
questionlinks[1]="../questions/what-is-the-difference-between-a-let-and-a-stroke.html";

function RandomQuestion(){
window.location=questionlinks[Math.floor(Math.random()*questionlinks.length)]
}