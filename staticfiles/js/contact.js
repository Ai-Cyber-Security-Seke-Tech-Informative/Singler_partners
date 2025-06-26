document.addEventListener("DOMContentLoaded", function() {
  const formElement = document.getElementById("contactForm");
  if (formElement) {
    const hasErrors = formElement.dataset.hasErrors === "true";
    const hasMessages = formElement.dataset.hasMessages === "true";

    if (hasErrors || hasMessages) {
      formElement.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }
});
