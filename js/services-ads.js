  const servicePromos = [
    {
      title: "✅ Enjoyed this article?",
      text: "Get a custom solo + pairs routine based on your weaknesses. Ideal for players stuck at a plateau.",
      link: "/personalised.html"
    },
    {
      title: "✅ Enjoyed this article?",
      text: "You might find my <a href="/videoanalysis.html">Video Analysis</a> service useful — get personalised feedback on your game without leaving your club.",
      link: "/videoanalysis.html"
    },
    {
      title: "✅ Enjoyed this article?",
      text: "Join hundreds of others trying new drills, games, and mindset tasks each month. Refresh your training routine!",
      link: "/challenges.html"
    },
    {
      title: "✅ Enjoyed this article?",
      text: "No more PDF printouts! Use our free timer app to stay on track during your solo sessions.",
      link: "/routinetimer.html"
    },
    {
      title: "✅ Enjoyed this article?",
      text: "Want focused solo sessions? Choose a series that matches your goals and court time.",
      link: "/soloroutines.html"
    }
  ];

  function insertServicePromo() {
    const promo = servicePromos[Math.floor(Math.random() * servicePromos.length)];
    const container = document.getElementById('service-cta');
    if (container) {
      container.innerHTML = `
        <div class="serviceads">
          <h2><strong>${promo.title}</strong></h2>
          <h2>${promo.text}</h2>
        </div>
      `;
    }
  }

  insertServicePromo();
