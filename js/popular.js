var poparticlelinks=new Array()

poparticlelinks[0]="/2022/20220804.html";
poparticlelinks[1]="/2022/20220621.html";
poparticlelinks[2]="/2022/20220919.html";
poparticlelinks[3]="/2022/20220730.html";
poparticlelinks[4]="/2022/20220912.html";
poparticlelinks[5]="/2022/20220903.html";
poparticlelinks[6]="/2022/20220812.html";
poparticlelinks[7]="/2022/20220904.html";
poparticlelinks[8]="/2022/20220831.html";
poparticlelinks[9]="/2022/20220628.html";
poparticlelinks[10]="/2022/20220910.html";
poparticlelinks[11]="/2022/20221125.html";

function RandomPopArticle(){
window.location=poparticlelinks[Math.floor(Math.random()*poparticlelinks.length)]
}