
// Wait for the DOM to be fully loaded
window.addEventListener('DOMContentLoaded', () => {
  const teamProfiles = [
    {
      name: "Seke Tech Genius",
      role: "Lead Ethical Hacker & Web Designer",
      description: "Mastermind behind our security architecture, blending coding prowess with visionary cyber defense.",
      image: "images/CCTV.avif"  // placeholder to avoid broken image during tests
    },
    {
      name: "Aria Quantum",
      role: "Quantum Cryptography Specialist",
      description: "Pioneering quantum-safe algorithms to future-proof our cybersecurity frameworks.",
      image: "images/hero.jpg"
    },
    {
      name: "Liam Cyberhawk",
      role: "AI Threat Analyst",
      description: "Using AI and ML to detect threats in real-time, ensuring proactive defense.",
      image: "images/CCTV.avif"
    },
    {
      name: "Maya Netshield",
      role: "Penetration Testing Lead",
      description: "Expert in finding vulnerabilities before attackers do, safeguarding client assets.",
      image: "images/CCTV.avif"
    },
    {
      name: "Ravi Codewalker",
      role: "Full Stack Security Developer",
      description: "Crafting secure applications that are both user-friendly and robust.",
      image: "images/CCTV.avif"
    }
  ];

  const container = document.getElementById('team-profile-container');
  if (!container) {
    console.error("Container with id 'team-profile-container' not found.");
    return;
  }

  let currentIndex = 0;

  function showProfile(index) {
    const profile = teamProfiles[index];
    if (!profile) {
      console.error(`No profile found at index ${index}`);
      return;
    }

    // Clear old content
    container.innerHTML = `
      <div class="team-profile">
        <img src="${profile.image}" alt="${profile.name}" 
             onerror="this.src='https://via.placeholder.com/150'; console.warn('Image not found: ${profile.image}')">
        <div class="info">
          <h3>${profile.name}</h3>
          <h4>${profile.role}</h4>
          <p>${profile.description}</p>
        </div>
      </div>
    `;

    // Schedule next profile after 5 seconds
    setTimeout(() => {
      currentIndex = (index + 1) % teamProfiles.length;
      showProfile(currentIndex);
    }, 5000);
  }

  showProfile(currentIndex); // initialize
});

// Accordion toggle logic with plus/minus icon
    document.querySelectorAll('.accordion-header').forEach(header => {
      header.addEventListener('click', () => {
        const accordion = header.parentElement;
        const allAccordions = [...document.querySelectorAll('.accordion')];
        if (accordion.classList.contains('active')) {
          accordion.classList.remove('active');
        } else {
          allAccordions.forEach(acc => acc.classList.remove('active'));
          accordion.classList.add('active');
        }
      });
    });