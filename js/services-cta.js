// service-cta.js
document.addEventListener('DOMContentLoaded', function() {
  // Get the service-cta div
  const serviceCta = document.getElementById('service-cta');
  
  // If the element doesn't exist on this page, exit
  if (!serviceCta) return;
  
  // Define the 5 different content options
  const options = [
    {
      title: "Enjoyed this article?",
      text: "You might find my <a href=\"/videoanalysis.html\">Video Analysis</a> service useful — get expert advice tailored to your specific needs."
    },
    {
      title: "Enjoyed this article?",
      text: "Our <a href=\"/videoanalysis.html\">Video Analysis</a> package provides priority assistance whenever you need it — 24/7 access to our team of experts."
    },
    {
      title: "Enjoyed this article?",
      text: "Take advantage of our <a href=\"/videoanalysis.html\">Video Analysis</a> service — have your system up and running in less than 24 hours."
    },
    {
      title: "Enjoyed this article?",
      text: "Don't miss our current <a href=\"/videoanalysis.html\">Video Analysis</a> — limited time discount available for all new customers this month."
    },
    {
      title: "Enjoyed this article?",
      text: "Get a <a href=\"/personalised.html\">Personlaised Practice Plan</a> that covers solo + pairs routines based on your weaknesses and objectives. Ideal for players stuck at a plateau."
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
    <div style="display: flex; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 36px; margin-right: 10px;">✅</span>
      <h2 style="font-weight: bold; margin: 0;">${randomOption.title}</h2>
    </div>
    <div style="font-size: 1.2em;">
      ${randomOption.text}
    </div>
  `;
});