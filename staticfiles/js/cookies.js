// ===== Helper functions =====
function setCookie(name, value, days) {
  let expires = "";
  if (days) {
    const d = new Date();
    d.setTime(d.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + d.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
  const nameEQ = name + "=";
  const ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

function eraseCookie(name) {
  document.cookie = name + "=; Max-Age=-99999999;";
}

// ===== Show/hide banner with animation =====
function showCookieBanner() {
  const banner = document.getElementById("cookieConsent");
  if (banner) {
    banner.style.opacity = 0;
    banner.style.display = "block";
    setTimeout(() => {
      banner.style.opacity = 1;
    }, 10); // slight delay to trigger CSS transition
  }
}

function hideCookieBanner() {
  const banner = document.getElementById("cookieConsent");
  if (banner) {
    banner.style.opacity = 0;
    setTimeout(() => {
      banner.style.display = "none";
    }, 500); // wait for fade-out transition to complete
  }
}

// ===== Check and show if no consent =====
function checkCookieConsent() {
  const consent = getCookie("cookie_consent");

  if (!consent) {
    showCookieBanner(); // Show immediately on page load (no delay)
  } else {
    hideCookieBanner(); // Hide if already accepted/rejected
  }
}

// ===== Button click logic =====
function setupCookieButtons() {
  const acceptBtn = document.getElementById("acceptCookies");
  const rejectBtn = document.getElementById("rejectCookies");

  if (acceptBtn) {
    acceptBtn.addEventListener("click", () => {
      setCookie("cookie_consent", "accepted", 365);
      hideCookieBanner();
      console.log("Cookies accepted");
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener("click", () => {
      setCookie("cookie_consent", "rejected", 365);
      hideCookieBanner();
      console.log("Cookies rejected");
    });
  }
}

// ===== Initialize =====
document.addEventListener("DOMContentLoaded", () => {
  checkCookieConsent();
  setupCookieButtons();
});
