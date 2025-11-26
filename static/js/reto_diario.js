    // Clave para identificar este reto específico
const STORAGE_KEY_RETO = 'reto_gracias_completado';

function horasDesde(timestamp) {
    const ahora = Date.now();
    return (ahora - timestamp) / (1000 * 60 * 60);
}

function actualizarEstadoReto() {
    const btn = document.getElementById('btn-completar-reto');
    const mensaje = document.getElementById('mensaje-reto');

    if (!btn || !mensaje) return;

    const datoGuardado = localStorage.getItem(STORAGE_KEY_RETO);

    if (!datoGuardado) {
        // Nunca se ha completado
        btn.disabled = false;
        mensaje.textContent = 'Cuando completes el reto, márcalo aquí para llevar tu progreso.';
        return;
    }

    const timestamp = parseInt(datoGuardado, 10);
    const horas = horasDesde(timestamp);

    if (horas >= 24) {
        // Han pasado más de 24 horas: puede volver a hacerlo
        btn.disabled = false;
        mensaje.textContent = 'Nuevo día, nuevo intento. Completa de nuevo el reto de “Gracias”.';
    } else {
        // Aún no han pasado 24 horas
        btn.disabled = true;
        const horasRestantes = Math.ceil(24 - horas);
        mensaje.textContent = `¡Ya completaste este reto! Vuelve en aproximadamente ${horasRestantes} hora(s).`;
    }
}

function marcarRetoComoCompletado() {
    const btn = document.getElementById('btn-completar-reto');
    const mensaje = document.getElementById('mensaje-reto');

    if (!btn || !mensaje) return;

    // Guardamos el momento actual
    localStorage.setItem(STORAGE_KEY_RETO, Date.now().toString());

    btn.disabled = true;
    mensaje.textContent = '¡Felicitaciones! Completaste el reto de hoy. Vuelve mañana para un nuevo reto.';
}

document.addEventListener('DOMContentLoaded', () => {
    actualizarEstadoReto();

    const btn = document.getElementById('btn-completar-reto');
    if (btn) {
        btn.addEventListener('click', marcarRetoComoCompletado);
    }
});
