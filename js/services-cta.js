// service-cta.js
document.addEventListener('DOMContentLoaded', function() {
  // Get the service-cta div
  const serviceCta = document.getElementById('service-cta');
  
  // If the element doesn't exist on this page, exit
  if (!serviceCta) return;
  
  // Define the 5 different content options
  const options = [
    {
      title: "Want to improve your ball control?",
      text: "These <a class=\"nointlink\" href=\"/soloroutines.html\">Solo Routines</a> help transform solo court time from filler into something focused and rewarding."
    },
    {
      title: "Make solo drilling easier with this free app?",
      text: "My FREE <a class=\"nointlink\" href=\"/routinetimer.html\">Routine Timer</a> app simplifies your solo training with one tap, but must be used with the <a class=\"nointlink\" href=\"/soloroutines.html\">Solo Routines</a>."
    },
    {
      title: "Looking to challenge yourself?",
      text: "The <a class=\"nointlink\" href=\"/challenges.html\">Monthly Squash Challenges</a> includes a blend of technical, tactical, and physical tasks, and will take your squash to the next level."
    },
    {
      title: "Want to hear the truth about your squash?",
      text: "You might find my <a class=\"nointlink\" href=\"/videoanalysis.html\">Video Analysis</a> service useful for highlighting patterns, habits, and blind spots that might otherwise go unnoticed."
    },
    {
      title: "There's nothing better than a customised training plan.",
      text: "Get a <a class=\"nointlink\" href=\"/personalised.html\">Personalised Practice Plan</a> that covers solo and pairs routines based on your objectives and weaker areas."
    }
  ];
  
  // Randomly select one of the options
  const randomOption = options[Math.floor(Math.random() * options.length)];
  
  
  // Create the HTML content
  serviceCta.innerHTML = `
    <div style="display: flex; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 36px; margin-right: 10px;">✅&nbsp;</span>
      <h2 style="font-weight: bold; margin: 0;">${randomOption.title}</h2>
    </div>
    <div style="font-size: 1.2em;">
      ${randomOption.text}
    </div>
  `;
});