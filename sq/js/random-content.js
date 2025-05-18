// Wait for DOM to be fully loaded before running
document.addEventListener('DOMContentLoaded', function() {
  // ===== TAGLINES SECTION =====
  const taglines = [
    "There are no silly questions. Just better squash.",
    "Curious minds play smarter.",
    "Because clarity beats guesswork.",
    "Asking is part of improving.",
    "Start with a question. End with a better game.",
    "Every good player stays curious."
  ];
  
  const taglineContainer = document.getElementById("tagline");
  
  // Only proceed with taglines if the container exists on this page
  if (taglineContainer) {
    // Create an aside element
    const asideElement = document.createElement('aside');
    
    // Get random tagline
    const randomIndex = Math.floor(Math.random() * taglines.length);
    asideElement.textContent = taglines[randomIndex];
    
    // You can add classes for styling if needed
    asideElement.className = "tagline-aside";
    
    // Clear the container and append the aside
    taglineContainer.innerHTML = '';
    taglineContainer.appendChild(asideElement);
  }

  // ===== FOOTER PROMOTIONS SECTION =====
  // Array of promotional content elements with their HTML
  const promotions = [
    `<p>🎯 SHARPEN YOUR BALL CONTROL with Solo Routines: Build precision and confidence by training in a way that isolates and strengthens your ball control. <a href="https://bettersquash.com/soloroutines.html">MASTER BALL PLACEMENT</a></p>`,
    
    `<p>💥 TIGHTEN YOU ADAPTIVE EDGE with Monthly Squash Challenges: Whether you train alone or with a partner, the challenges offer tough, realistic scenarios to sharpen your performance. <a href="https://bettersquash.com/challenges.html">PUSH YOUR LIMITS</a></p>`,
    
    `<p>📝 ADDRESS YOUR TECHNICAL PRIORITIES with Personalised Practice Plans: These plans give you focused training sessions built around your goals and current weaknesses. <a href="https://bettersquash.com/personalised.html">TARGET YOUR WEAKNESSES</a></p>`,
    
    `<p>🎬 SHARPEN YOUR TACTICS & COURTCRAFT with Video Analysis: Understand your patterns and fix costly mistakes by watching your own game from a coach's perspective. <a href="https://bettersquash.com/videoanalysis.html">SEE WHAT YOU'RE MISSING</a></p>`
  ];
  
  // Get the container where the promotion will be displayed
  const promotionContainer = document.getElementById("footer-promotion");
  
  // Only proceed with promotions if the container exists on this page
  if (promotionContainer) {
    // Select a random promotion
    const randomIndex = Math.floor(Math.random() * promotions.length);
    
    // Set the HTML content
    promotionContainer.innerHTML = promotions[randomIndex];
  }
});