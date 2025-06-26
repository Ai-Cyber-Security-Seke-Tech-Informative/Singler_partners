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
