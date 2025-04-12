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
      text: "<a href=\"/soloroutines.html\">Solo Routines</a> help transform solo court time from filler into something focused and rewarding.<br><br>These sessions are designed to make practice more productive by giving you a clear structure to follow, with emphasis on movement, shot quality, and timing."
    },
    {
      title: " Enjoyed this article?",
      text: "<a href=\"/routinetimer.html\">The Routine Timer companion app</a> simplifies your solo training with one tap.<br><br>It handles the timings and transitions so you don’t have to stop and think. You just practice."
    },
    {
      title: " Enjoyed this article?",
      text: "The <a href=\"/challenges.html\">Monthly Squash Challenges</a>  offer something fresh to aim for.<br><br>Each group includes a blend of technical, tactical, and physical tasks - ranging from solo drills to match play rules and mental toughness tests."
    },
    {
      title: " Enjoyed this article?",
      text: "You might find my <a href=\"/videoanalysis.html\">Video Analysis</a> service useful. By reviewing your matches or drills, I highlight patterns, habits, and blind spots that might otherwise go unnoticed."
    },
    {
      title: " Enjoyed this article?",
      text: "Get a <a href=\"/personalised.html\">Personalised Practice Plan</a> that covers solo and pairs routines based on your objectives and weaker areas.<br><br>Ideal for players stuck at a plateau or for somebody looking to take their game to the next level.."
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