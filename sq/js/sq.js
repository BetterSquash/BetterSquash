// Wait for DOM to be fully loaded before running
document.addEventListener('DOMContentLoaded', function() {
	// Array of promotional content elements with their HTML
	const promotions = [
		`<p>🎯 SHARPEN YOUR BALL CONTROL with Solo Routines: Build precision and confidence by training in a way that isolates and strengthens your ball control. <a href="https://bettersquash.com/soloroutines.html">MASTER BALL PLACEMENT</a></p>`,
		`<p>💥 TIGHTEN YOU ADAPTIVE EDGE with Monthly Squash Challenges: Whether you train alone or with a partner, the challenges offer tough, realistic scenarios to sharpen your performance. <a href="https://bettersquash.com/challenges.html">PUSH YOUR LIMITS</a></p>`,
		`<p>🎯 SHARPEN YOUR BALL CONTROL with Solo Routines: Build precision and confidence by training in a way that isolates and strengthens your ball control. <a href="https://bettersquash.com/soloroutines.html">MASTER BALL PLACEMENT</a></p>`,
		`<p>📝 ADDRESS YOUR TECHNICAL PRIORITIES with Personalised Practice Plans: These plans give you focused training sessions built around your goals and current weaknesses. <a href="https://bettersquash.com/personalised.html">TARGET YOUR WEAKNESSES</a></p>`,
		`<p>🎯 SHARPEN YOUR BALL CONTROL with Solo Routines: Build precision and confidence by training in a way that isolates and strengthens your ball control. <a href="https://bettersquash.com/soloroutines.html">MASTER BALL PLACEMENT</a></p>`,
		`<p>🎬 REFINE YOUR TACTICS & COURTCRAFT with Video Analysis: Understand your patterns and fix costly mistakes by watching your own game from a coach's perspective. <a href="https://bettersquash.com/videoanalysis.html">SEE WHAT YOU'RE MISSING</a></p>`
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

document.addEventListener('DOMContentLoaded', function() {
  // Arrays of real URLs
  const randomQuestions = [
    "../questions/does-the-ball-have-to-bounce-in-squash.html",
    "../questions/what-is-the-difference-between-a-let-and-a-stroke.html"
  ];

  const popularQuestions = [
    "../questions/what-is-a-drop-shot.html",
    "../questions/how-do-you-serve-in-squash.html"
  ];

  // Replace Random Link
  const randomLink = document.getElementById("RandomLink");
  if (randomLink && randomQuestions.length > 0) {
    const randomIndex = Math.floor(Math.random() * randomQuestions.length);
    randomLink.href = randomQuestions[randomIndex];
  }

  // Replace Popular Link
  const popularLink = document.getElementById("PopularLink");
  if (popularLink && popularQuestions.length > 0) {
    const popularIndex = Math.floor(Math.random() * popularQuestions.length);
    popularLink.href = popularQuestions[popularIndex];
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const banner = document.getElementById('cookie-banner');
  const acceptBtn = document.getElementById('accept-cookies');
  const declineBtn = document.getElementById('decline-cookies');

  if (!localStorage.getItem('cookieConsent')) {
    banner.style.display = 'block';
  } else {
    banner.remove();
  }

  if (acceptBtn) {
    acceptBtn.addEventListener('click', function () {
      localStorage.setItem('cookieConsent', 'accepted');
      banner.remove();
    });
  }

  if (declineBtn) {
    declineBtn.addEventListener('click', function () {
      localStorage.setItem('cookieConsent', 'declined');
      banner.remove();
    });
  }
});

