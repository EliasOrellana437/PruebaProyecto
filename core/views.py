from django.shortcuts import render, redirect
from django.http import Http404

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        # Guardamos el nombre en sesión para mostrarlo en el menú
        request.session['username'] = username or 'Invitado'
        return redirect('menu')
    return render(request, 'core/login.html')  # muestra el formulario

def menu_view(request):
    username = request.session.get('username', 'Invitado')
    options = [
        {'slug': 'leccion-basica', 'title': 'Lección básica de alfabeto', 'desc': 'Aprende A–Z con gestos.'},
        {'slug': 'mini-juego-memoria', 'title': 'Mini juego de memoria', 'desc': 'Asocia gesto con letra.'},
        {'slug': 'practica-numeros', 'title': 'Práctica de números', 'desc': 'Del 0 al 9 en LSC/ASL.'},
        {'slug': 'retos-diarios', 'title': 'Retos diarios', 'desc': 'Pequeños objetivos gamificados.'},
    ]
    return render(request, 'core/menu.html', {'username': username, 'options': options})

#apartado de retos diarios
def retos_diarios_view(request):
    return render(request, 'core/retos_diarios.html')
{'slug': 'retos-diarios', 'title': 'Retos diarios', 'desc': 'Pequeños objetivos gamificados.'},

#apartado para frases utiles
# Catálogo base (puedes editar y ampliar)
FRASES_CATALOGO = [
    {
        "slug": "gracias",
        "titulo": "Gracias",
        "descripcion": "Expresa gratitud con esta seña.",
        "media": "img/frase_gracias.gif",
        "explicacion": "La mano parte desde la boca y se proyecta hacia afuera.",
        "contexto": "Usa esta seña para agradecer a alguien de forma clara.",
    },
    {
        "slug": "hola",
        "titulo": "Hola",
        "descripcion": "Saluda usando señas.",
        "media": "img/frase_hola.gif",
        "explicacion": "Movimiento de la mano abierta en señal de saludo.",
        "contexto": "Apta para saludos informales y formales.",
    },
    {
        "slug": "como-estas",
        "titulo": "¿Cómo estás?",
        "descripcion": "Pregunta por el estado de alguien.",
        "media": "img/frase_como_estas.gif",
        "explicacion": "Gestos encadenados para preguntar por el estado.",
        "contexto": "Útil en conversaciones cotidianas.",
    },
]

def frases_utiles(request):
    return render(request, 'core/frases_utiles.html', {
        "titulo": "Frases útiles",
        "descripcion": "Explora frases cotidianas y aprende su seña.",
        "frases": FRASES_CATALOGO,
    })

def frase_detalle(request, slug):
    frase = next((f for f in FRASES_CATALOGO if f["slug"] == slug), None)
    if not frase:
        raise Http404("Frase no encontrada")

    return render(request, 'core/frase_detalle.html', {
        "frase": frase,
        "titulo": frase["titulo"],
    })
