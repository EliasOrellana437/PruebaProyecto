//  Línea temporal para confirmar que el JS nuevo se está cargando
console.log("JS NUEVO CARGADO");

document.querySelectorAll('.tile').forEach(tile => {
  const href = tile.getAttribute('href');

  // Si el enlace es falso (vacío, #, undefined), bloqueamos el clic
  if (!href || href === '#' || href === 'undefined') {
    tile.addEventListener('click', (e) => {
      e.preventDefault();
      const slug = tile.dataset.slug || 'esta función';
      alert(`Esta función (${slug}) llegará en el siguiente sprint.`);
    });
  }

  // Si el enlace es real, dejamos que el navegador lo siga
});
