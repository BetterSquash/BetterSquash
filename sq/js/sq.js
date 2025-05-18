// Wait for DOM to be fully loaded before running
document.addEventListener('DOMContentLoaded', function() {
  // Array of promotional content elements with their HTML
  const promotions = [
    `<p>🎯 SHARPEN YOUR BALL CONTROL with Solo Routines: Build precision and confidence by training in a way that isolates and strengthens your ball control. <a href="">MASTER BALL PLACEMENT</a></p>`,
    
    `<p>💥 TIGHTEN YOU ADAPTIVE EDGE with Monthly Squash Challenges: Whether you train alone or with a partner, the challenges offer tough, realistic scenarios to sharpen your performance. <a href="">PUSH YOUR LIMITS</a></p>`,
    
    `<p>📝 ADDRESS YOUR TECHNICAL PRIORITIES with Personalised Practice Plans: These plans give you focused training sessions built around your goals and current weaknesses. <a href="">TARGET YOUR WEAKNESSES</a></p>`,
    
    `<p>🎬 SHARPEN YOUR TACTICS & COURTCRAFT with Video Analysis: Understand your patterns and fix costly mistakes by watching your own game from a coach's perspective. <a href="">SEE WHAT YOU'RE MISSING</a></p>`
  ];
  
  // Get the container where the promotion will be displayed
  const promotionContainer = document.getElementById("footer-promotion");
  
  // Only proceed if the promotion container exists on this page
  if (promotionContainer) {
    // Select a random promotion
    const randomIndex = Math.floor(Math.random() * promotions.length);
    
    // Set the HTML content
    promotionContainer.innerHTML = promotions[randomIndex];
  }
});













document.addEventListener('DOMContentLoaded', function() {
  const checkButtons = document.querySelectorAll('.reveal-answers');
  checkButtons.forEach(button => {
    const answers = button.parentElement.querySelector('.answers');
    if (answers) {
      button.addEventListener('click', () => {
        answers.classList.toggle('hidden');
        button.textContent = answers.classList.contains('hidden') ? 'Show Answers' : 'Hide Answers';
      });
    }
  });
});


var questionlinks=new Array()

questionlinks[0]="../questions/does-the-ball-have-to-bounce-in-squash.html";
questionlinks[1]="../questions/what-is-the-difference-between-a-let-and-a-stroke.html";

function RandomQuestion(){
window.location=questionlinks[Math.floor(Math.random()*questionlinks.length)]
}