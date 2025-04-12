// service-cta.js
document.addEventListener('DOMContentLoaded', function() {
  // Get the service-cta div
  const serviceCta = document.getElementById('service-cta');
  
  // If the element doesn't exist on this page, exit
  if (!serviceCta) return;
  
  // Define the 5 different content options
  const options = [
    {
      title: "Professional Consultation",
      text: "You might find my <a href=\"/consultation.html\">Professional Consultation</a> service useful — get expert advice tailored to your specific needs."
    },
    {
      title: "Premium Support",
      text: "Our <a href=\"/premium-support.html\">Premium Support</a> package provides priority assistance whenever you need it — 24/7 access to our team of experts."
    },
    {
      title: "Quick Installation",
      text: "Take advantage of our <a href=\"/quick-install.html\">Quick Installation</a> service — have your system up and running in less than 24 hours."
    },
    {
      title: "Special Offer",
      text: "Don't miss our current <a href=\"/special-offers.html\">Special Offer</a> — limited time discount available for all new customers this month."
    },
    {
      title: "Video Analysis",
      text: "You might find my <a href=\"/videoanalysis.html\">Video Analysis</a> service useful — get personalised feedback on your game without leaving your club."
    }
  ];
  
  // Randomly select one of the options
  const randomOption = options[Math.floor(Math.random() * options.length)];
  
  // Apply styling to the container
  serviceCta.style.borderLeft = '3px solid';
  serviceCta.style.backgroundColor = '#FDFDFD';
  serviceCta.style.padding = '15px';
  serviceCta.style.margin = '20px 0';
  
  // Create the HTML content
  serviceCta.innerHTML = `
    <div style="display: flex; align-items: center; margin-bottom: 8px;">
      <span style="font-size: 24px; margin-right: 10px;">✅</span>
      <h2 style="font-weight: bold; margin: 0;">${randomOption.title}</h2>
    </div>
    <div style="font-size: 1.2em;">
      ${randomOption.text}
    </div>
  `;
});