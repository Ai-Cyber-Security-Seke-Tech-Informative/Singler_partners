

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