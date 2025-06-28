
document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navMenu = document.getElementById("nav-menu");
  const closeMenu = document.getElementById("close-menu");
  const body = document.body;

  // Open menu
  if (menuToggle && navMenu && closeMenu) {
    menuToggle.addEventListener("click", () => {
      navMenu.classList.add("active");
      menuToggle.setAttribute("aria-expanded", "true");
      body.classList.add("menu-open"); // disable scroll
    });

    // Close menu
    closeMenu.addEventListener("click", () => {
      navMenu.classList.remove("active");
      menuToggle.setAttribute("aria-expanded", "false");
      body.classList.remove("menu-open"); // enable scroll

      // Collapse all dropdowns
      document.querySelectorAll(".dropdown").forEach(d => {
        d.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Dropdown toggle on mobile
  const dropdowns = document.querySelectorAll(".dropdown");

  dropdowns.forEach((dropdown) => {
    const link = dropdown.querySelector("a");

    if (link) {
      link.addEventListener("click", (e) => {
        if (window.innerWidth <= 880) {
          e.preventDefault();

          const isExpanded = dropdown.getAttribute("aria-expanded") === "true";

          // Close all others
          dropdowns.forEach(d => d.setAttribute("aria-expanded", "false"));

          // Open clicked one
          dropdown.setAttribute("aria-expanded", isExpanded ? "false" : "true");
        }
      });
    }
  });

  // Optional: collapse menu & dropdowns on resize up to desktop
  window.addEventListener("resize", () => {
    if (window.innerWidth > 880) {
      body.classList.remove("menu-open");
      navMenu?.classList.remove("active");
      menuToggle?.setAttribute("aria-expanded", "false");

      dropdowns.forEach(d => d.setAttribute("aria-expanded", "false"));
    }
  });
});

  // Intersection Observer to add 'visible' class on scroll
  const blocks = document.querySelectorAll('.fade-in');
  const options = {
    threshold: 0.1,
  };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, options);

  blocks.forEach(block => {
    observer.observe(block);
  });

  // Optional but highly recommended for MEGAMIND experience
document.querySelectorAll('.megamind-block').forEach(block => {
  block.addEventListener('mousemove', (e) => {
    const rect = block.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    // Calculate rotation, max 15 deg
    const rotateX = ((y - centerY) / centerY) * 10;
    const rotateY = ((x - centerX) / centerX) * 15;

    block.style.transform = `rotateX(${-rotateX}deg) rotateY(${rotateY}deg) translateZ(40px)`;
  });

  block.addEventListener('mouseleave', () => {
    block.style.transform = 'translateZ(40px) rotateX(4deg) rotateY(8deg)';
  });
});

// Background gradient subtle shift based on mouse move
document.body.addEventListener('mousemove', e => {
  const x = e.clientX / window.innerWidth;
  const y = e.clientY / window.innerHeight;

  document.body.style.background = `
    linear-gradient(120deg, 
    azure,${0.8 + 0.2 * y}), 
    white,${0.7 + 0.3 * x}))`;
});

 // Scroll to top functionality
  document.querySelector('.scroll-top').addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // hero-slider.js

let currentSlide = 0;
const slides = document.querySelectorAll('.hero-slide');
const totalSlides = slides.length;
const intervalTime = 6000; // 6 seconds
let slideInterval;

// Typewriter animation on heading
function typeWriter(text, element, delay = 75) {
  element.innerHTML = '';
  let i = 0;
  function typing() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(typing, delay);
    }
  }
  typing();
}

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    slide.classList.remove('animate-fade', 'animate-zoom', 'animate-rise', 'animate-shift', 'animate-blur');
    if (i === index) {
      slide.classList.add('active');
      const animation = slide.getAttribute('data-animation');
      slide.classList.add(animation);

      const heading = slide.querySelector('h1');
      if (heading) {
        typeWriter(heading.getAttribute('data-text'), heading);
      }
    }
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  showSlide(currentSlide);
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  showSlide(currentSlide);
}

document.getElementById('prevSlide').addEventListener('click', () => {
  prevSlide();
  resetInterval();
});

document.getElementById('nextSlide').addEventListener('click', () => {
  nextSlide();
  resetInterval();
});

function startSlider() {
  slideInterval = setInterval(nextSlide, intervalTime);
}

function resetInterval() {
  clearInterval(slideInterval);
  startSlider();
}

// Initial call
showSlide(currentSlide);
startSlider();

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
    


  window.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('team-profile-container');
    if (!container) {
      console.error("Container not found.");
      return;
    }

    // Load Django static paths from data- attributes
    const STATIC_IMAGES = {
      SEKE: container.dataset.seke || 'https://via.placeholder.com/150?text=SEKE',
      HERO: container.dataset.hero || 'https://via.placeholder.com/150?text=HERO',
      CCTV: container.dataset.cctv || 'https://via.placeholder.com/150?text=CCTV'
    };

    const teamProfiles = [
      {
        name: "Seke Tech Genius",
        role: "Lead Ethical Hacker & Web Designer",
        description: "Mastermind behind our security architecture.",
        image: STATIC_IMAGES.SEKE || STATIC_IMAGES.SEKE  // Typo fallback
      },
      {
        name: "Aria Quantum",
        role: "Quantum Cryptography Specialist",
        description: "Future-proofing cybersecurity.",
        image: STATIC_IMAGES.HERO
      },
      {
        name: "Liam Cyberhawk",
        role: "AI Threat Analyst",
        description: "Real-time threat detection.",
        image: STATIC_IMAGES.CCTV
      },
      {
        name: "Maya Netshield",
        role: "Penetration Testing Lead",
        description: "Safeguarding assets.",
        image: STATIC_IMAGES.CCTV
      },
      {
        name: "Ravi Codewalker",
        role: "Full Stack Security Developer",
        description: "Secure, user-friendly apps.",
        image: STATIC_IMAGES.HERO
      }
    ];

    let currentIndex = 0;

    function showProfile(index) {
      const profile = teamProfiles[index];

      container.innerHTML = `
        <div class="team-profile">
          <img src="${profile.image}" alt="${profile.name}"
               onerror="this.src='https://via.placeholder.com/150?text=No+Image'">
          <div class="info">
            <h3>${profile.name}</h3>
            <h4>${profile.role}</h4>
            <p>${profile.description}</p>
          </div>
        </div>
      `;

      // Cycle to next profile
      setTimeout(() => {
        currentIndex = (index + 1) % teamProfiles.length;
        showProfile(currentIndex);
      }, 5000);
    }

    // Start
    showProfile(currentIndex);
  });



