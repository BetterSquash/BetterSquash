// Wait for DOM to be fully loaded before running
document.addEventListener('DOMContentLoaded', function() {
  const taglines = [
    "There are no silly questions. Just better squash.",
    "Curious minds play smarter.",
    "Because clarity beats guesswork.",
    "Asking is part of improving.",
    "Start with a question. End with a better game.",
    "Every good player stays curious."
  ];
  
  const taglineContainer = document.getElementById("tagline");
  
  // Only proceed if the tagline container exists on this page
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
});