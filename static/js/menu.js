document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.tile').forEach(tile => {
    tile.addEventListener('click', (e) => {
      e.preventDefault();
      const slug = tile.dataset.slug;
      alert(`Esta función (${slug}) llegará en el siguiente sprint.`);
    });
  });
});
