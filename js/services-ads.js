<script>
  const servicePromos = [
    {
      title: "🎯 Personalised Practice Plans",
      text: "Get a custom solo + pairs routine based on your weaknesses. Ideal for players stuck at a plateau.",
      link: "/personalised.html"
    },
    {
      title: "📹 Video Analysis",
      text: "Upload your game and get targeted feedback within 48 hours. Available in short-form and full-form versions.",
      link: "/video-analysis.html"
    },
    {
      title: "🧠 Monthly Challenges",
      text: "Join hundreds of others trying new drills, games, and mindset tasks each month. Refresh your training routine!",
      link: "/challenges.html"
    },
    {
      title: "⏱️ Routine Timer App",
      text: "No more PDF printouts! Use our free timer app to stay on track during your solo sessions.",
      link: "/routinetimer.html"
    },
    {
      title: "🏋️ Solo Routines",
      text: "Want focused solo sessions? Choose a series that matches your goals and court time.",
      link: "/soloroutines.html"
    }
  ];

  function insertServicePromo() {
    const promo = servicePromos[Math.floor(Math.random() * servicePromos.length)];
    const container = document.getElementById('service-cta');
    if (container) {
      container.innerHTML = `
        <div style="border-top: 1px solid #ccc; margin-top: 3rem; padding-top: 1.5rem; font-family: sans-serif;">
          <strong>${promo.title}</strong><br>
          <span>${promo.text}</span><br>
          <a href="${promo.link}" style="color: #02386E; text-decoration: underline;">Learn more</a>
        </div>
      `;
    }
  }

  insertServicePromo();
</script>