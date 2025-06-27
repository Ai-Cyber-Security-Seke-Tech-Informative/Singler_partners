document.addEventListener("DOMContentLoaded", () => {
  const participantsModal = document.getElementById("participantsModal");
  const btnViewParticipants = document.getElementById("btnViewParticipants");
  const btnCloseParticipantsModal = document.getElementById("closeParticipantsModal");
  const searchInput = document.getElementById("searchConversations");
  const conversationsList = document.getElementById("conversationsList");

  if (btnViewParticipants) {
    btnViewParticipants.addEventListener("click", () => {
      participantsModal.classList.remove("hidden");
    });
  }

  if (btnCloseParticipantsModal) {
    btnCloseParticipantsModal.addEventListener("click", () => {
      participantsModal.classList.add("hidden");
    });
  }

  if (searchInput && conversationsList) {
    searchInput.addEventListener("input", () => {
      const filter = searchInput.value.toLowerCase();
      [...conversationsList.children].forEach((item) => {
        if (item.textContent.toLowerCase().includes(filter)) {
          item.style.display = "";
        } else {
          item.style.display = "none";
        }
      });
    });
  }

  // You can add message sending with AJAX here,
  // or WebSocket real-time typing indicator updates
});


  document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('.nav-menu a');

    // Load last active from localStorage
    const activeHref = localStorage.getItem('activeLink');
    if (activeHref) {
      links.forEach(link => {
        if (link.getAttribute('href') === activeHref) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }

    // Listen for link clicks
    links.forEach(link => {
      link.addEventListener('click', () => {
        localStorage.setItem('activeLink', link.getAttribute('href'));
        links.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
      });
    });
  });

function toggleDropdown(id) {
  const el = document.getElementById(id);
  if (!el) return;

  const isVisible = el.classList.toggle('show');
  el.style.display = isVisible ? 'block' : 'none';

  // Update aria-expanded on the trigger button
  const triggers = document.querySelectorAll('[aria-controls="' + id + '"]');
  triggers.forEach(trigger => {
    trigger.setAttribute('aria-expanded', isVisible);
  });
}

function openNotificationDetail(pk, title, message, type, sender, date, url) {
  const dropdown = document.getElementById('notifDropdown');
  if (dropdown) {
    dropdown.classList.remove('show');
    dropdown.style.display = 'none';
    Array.from(dropdown.children).forEach(child => {
      child.style.display = 'none';
    });
  }

  const detailCard = document.getElementById('notifDetailCard');
  if (detailCard) {
    detailCard.style.display = 'block';
    detailCard.style.zIndex = '1100';
  }

  document.getElementById('detailTitle').textContent = title;
  document.getElementById('detailMessage').textContent = message;
  document.getElementById('detailType').textContent = type;
  document.getElementById('detailSender').textContent = sender;
  document.getElementById('detailDate').textContent = date;

  const urlEl = document.getElementById('detailUrl');
  const urlContainer = document.getElementById('detailUrlContainer');

  if (url && url.trim() !== "") {
    urlEl.href = url;
    urlEl.textContent = url;
    urlContainer.style.display = 'block';
  } else {
    urlContainer.style.display = 'none';
  }

  const formEl = document.getElementById('deleteNotificationForm');
  if (formEl) {
    formEl.action = `/notifications/delete/${pk}/`;
  }
}

function closeNotificationDetail() {
  const detailCard = document.getElementById('notifDetailCard');
  if (detailCard) detailCard.style.display = 'none';

  const dropdown = document.getElementById('notifDropdown');
  if (dropdown) {
    dropdown.style.display = 'block';
    dropdown.classList.add('show');
    Array.from(dropdown.children).forEach(child => {
      child.style.display = 'block';
    });
  }
}

 document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".nav-menu a");

    // Function to activate clicked link
    function activateLink(link) {
      navLinks.forEach(l => l.classList.remove("active"));
      link.classList.add("active");

      // On small screens: scroll to center of clicked link
      if (window.innerWidth <= 600) {
        link.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
      }
    }

    // Handle SPA-style clicks
    navLinks.forEach(link => {
      link.addEventListener("click", function (e) {
        // Optional: prevent scroll jump for internal nav
        if (link.getAttribute("href").startsWith("#") || link.closest('[data-spa]')) {
          e.preventDefault();
          activateLink(link);

          // If you’re using anchors or AJAX updates, handle them here:
          const targetId = link.getAttribute("href").slice(1);
          const targetEl = document.getElementById(targetId);
          if (targetEl) {
            targetEl.scrollIntoView({ behavior: "smooth" });
          }
        }
      });
    });

    // Optional: restore last active link (e.g. after SPA reload)
    const storedHref = localStorage.getItem("activeNavHref");
    if (storedHref) {
      const storedLink = [...navLinks].find(link => link.href === storedHref);
      if (storedLink) activateLink(storedLink);
    }

    // Store active link persistently
    navLinks.forEach(link => {
      link.addEventListener("click", () => {
        localStorage.setItem("activeNavHref", link.href);
      });
    });
  });