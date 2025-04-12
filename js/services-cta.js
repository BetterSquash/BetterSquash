// service-cta.js
document.addEventListener('DOMContentLoaded', function() {
  // Get the service-cta div
  const serviceCta = document.getElementById('service-cta');
  
  // If the element doesn't exist on this page, exit
  if (!serviceCta) return;
  
  // Define the 5 different content options
  const options = [
    {
      title: " Enjoyed this article?",
      text: "<a href=\"/soloroutines.html\">Solo Routines</a> help transform solo court time from filler into something focused and rewarding."
    },
    {
      title: " Enjoyed this article?",
      text: "My FREE <a href=\"/routinetimer.html\">Routine Timer</a> app simplifies your solo training with one tap."
    },
    {
      title: " Enjoyed this article?",
      text: "The <a href=\"/challenges.html\">Monthly Squash Challenges</a> includes a blend of technical, tactical, and physical tasks."
    },
    {
      title: " Enjoyed this article?",
      text: "You might find my <a href=\"/videoanalysis.html\">Video Analysis</a> service useful for highlighting patterns, habits, and blind spots that might otherwise go unnoticed."
    },
    {
      title: " Enjoyed this article?",
      text: "Get a <a href=\"/personalised.html\">Personalised Practice Plan</a> that covers solo and pairs routines based on your objectives and weaker areas."
    }
  ];
  
  // Randomly select one of the options
  const randomOption = options[Math.floor(Math.random() * options.length)];
  
  // Apply styling to the container
  serviceCta.style.borderLeft = '3px solid';
  serviceCta.style.backgroundColor = '#EEEEE';
  serviceCta.style.padding = '15px';
  serviceCta.style.margin = '20px 0';
  
  // Create the HTML content
  serviceCta.innerHTML = `
    <div style="display: flex; align-items: center; margin-bottom: 12px;>
      <span style="font-size: 36px; margin-right: 10px;">✅</span>
      <h2 style="font-weight: bold; margin: 0;">${randomOption.title}</h2>
    </div>
    <div style="font-size: 1.2em;">
      ${randomOption.text}
    </div>
  `;
});