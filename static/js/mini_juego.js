document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".quiz-item");

  items.forEach(item => {
    const respuesta = item.dataset.respuesta;
    const botones = item.querySelectorAll(".quiz-btn");
    const feedback = item.querySelector(".quiz-feedback");

    botones.forEach(btn => {
      btn.addEventListener("click", () => {
        if (btn.textContent === respuesta) {
          feedback.textContent = "Correcto!";
          feedback.style.color = "limegreen";
        } else {
          feedback.textContent = `Incorrecto. La respuesta era: ${respuesta}`;
          feedback.style.color = "red";
        }
        // Desactivar botones después de responder
        botones.forEach(b => b.disabled = true);
      });
    });
  });
});
