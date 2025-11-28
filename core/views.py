from django.shortcuts import render, redirect
import random
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

#apartado mini juego
QUIZ_ITEMS = [
    {
        "slug": "a",
        "tipo": "letra",
        "titulo": "Letra A",
        "media": "img/A.gif",
        "opciones": ["A", "B", "C"],
        "respuesta": "A",
    },
    {
        "slug": "b",
        "tipo": "letra",
        "titulo": "Letra B",
        "media": "img/B.gif",
        "opciones": ["A", "B", "D"],
        "respuesta": "B",
    },
    {
        "slug": "c",
        "tipo": "letra",
        "titulo": "Letra C",
        "media": "img/C.gif",
        "opciones": ["C", "D", "E"],
        "respuesta": "C",
    },
    {
        "slug": "d",
        "tipo": "letra",
        "titulo": "Letra D",
        "media": "img/D.gif",
        "opciones": ["D", "Z", "F"],
        "respuesta": "D",
    },
    {
        "slug": "e",
        "tipo": "letra",
        "titulo": "Letra E",
        "media": "img/E.gif",
        "opciones": ["H", "J", "E"],
        "respuesta": "E",
    },
    {
        "slug": "f",
        "tipo": "letra",
        "titulo": "Letra F",
        "media": "img/F.gif",
        "opciones": ["F", "K", "M"],
        "respuesta": "F",
    },
    {
        "slug": "g",
        "tipo": "letra",
        "titulo": "Letra G",
        "media": "img/G.gif",
        "opciones": ["G", "V", "R"],
        "respuesta": "G",
    },
    {
        "slug": "h",
        "tipo": "letra",
        "titulo": "Letra H",
        "media": "img/H.gif",
        "opciones": ["H", "P", "N"],
        "respuesta": "H",
    },
    {
        "slug": "i",
        "tipo": "letra",
        "titulo": "Letra I",
        "media": "img/I.gif",
        "opciones": ["C", "I", "W"],
        "respuesta": "I",
    },
    {
        "slug": "j",
        "tipo": "letra",
        "titulo": "Letra J",
        "media": "img/J.gif",
        "opciones": ["S", "A", "J"],
        "respuesta": "J",
    },
    {
        "slug": "k",
        "tipo": "letra",
        "titulo": "Letra K",
        "media": "img/K.gif",
        "opciones": ["X", "Ñ", "K"],
        "respuesta": "K",
    },
    {
        "slug": "l",
        "tipo": "letra",
        "titulo": "Letra L",
        "media": "img/L.gif",
        "opciones": ["L", "Q", "O"],
        "respuesta": "L",
    },
    {
        "slug": "m",
        "tipo": "letra",
        "titulo": "Letra M",
        "media": "img/M.gif",
        "opciones": ["Ñ", "M", "A"],
        "respuesta": "M",
    },
    {
        "slug": "n",
        "tipo": "letra",
        "titulo": "Letra N",
        "media": "img/N.gif",
        "opciones": ["J", "N", "P"],
        "respuesta": "N",
    },
    {
        "slug": "ñ",
        "tipo": "letra",
        "titulo": "Letra Ñ",
        "media": "img/Ñ.gif",
        "opciones": ["Z", "Ñ", "V"],
        "respuesta": "Ñ",
    },
    {
        "slug": "o",
        "tipo": "letra",
        "titulo": "Letra O",
        "media": "img/O.gif",
        "opciones": ["V", "L", "O"],
        "respuesta": "O",
    },
    {
        "slug": "p",
        "tipo": "letra",
        "titulo": "Letra P",
        "media": "img/P.gif",
        "opciones": ["P", "B", "D"],
        "respuesta": "P",
    },
    {
        "slug": "q",
        "tipo": "letra",
        "titulo": "Letra Q",
        "media": "img/Q.gif",
        "opciones": ["K", "Q", "T"],
        "respuesta": "C",
    },
        {
        "slug": "r",
        "tipo": "letra",
        "titulo": "Letra R",
        "media": "img/R.gif",
        "opciones": ["R", "Y", "U"],
        "respuesta": "Ñ",
    },
    {
        "slug": "s",
        "tipo": "letra",
        "titulo": "Letra S",
        "media": "img/S.gif",
        "opciones": ["S", "U", "G"],
        "respuesta": "S",
    },
    {
        "slug": "t",
        "tipo": "letra",
        "titulo": "Letra T",
        "media": "img/T.gif",
        "opciones": ["L", "C", "T"],
        "respuesta": "T",
    },
    {
        "slug": "u",
        "tipo": "letra",
        "titulo": "Letra U",
        "media": "img/U.gif",
        "opciones": ["U", "Y", "B"],
        "respuesta": "U",
    },
        {
        "slug": "v",
        "tipo": "letra",
        "titulo": "Letra V",
        "media": "img/V.gif",
        "opciones": ["U", "Y", "V"],
        "respuesta": "V",
    },
    {
        "slug": "w",
        "tipo": "letra",
        "titulo": "Letra W",
        "media": "img/W.gif",
        "opciones": ["N", "Z", "W"],
        "respuesta": "W",
    },
    {
        "slug": "X",
        "tipo": "letra",
        "titulo": "Letra X",
        "media": "img/X.gif",
        "opciones": ["J", "A", "X"],
        "respuesta": "X",
    },
        {
        "slug": "y",
        "tipo": "letra",
        "titulo": "Letra Y",
        "media": "img/Y.gif",
        "opciones": ["Q", "Y", "R"],
        "respuesta": "Y",
    },
    {
        "slug": "z",
        "tipo": "letra",
        "titulo": "Letra Z",
        "media": "img/Z.gif",
        "opciones": ["W", "L", "Z"],
        "respuesta": "Z",
    },
    {
        "slug": "gracias",
        "tipo": "frase",
        "titulo": "Frase: Gracias",
        "media": "img/frase_gracias.gif",
        "opciones": ["Hola", "Gracias", "Perdón"],
        "respuesta": "Gracias",
    },
    {
        "slug": "hola",
        "tipo": "frase",
        "titulo": "Frase: Hola",
        "media": "img/frase_hola.gif",
        "opciones": ["Hola", "Adiós", "Gracias"],
        "respuesta": "Hola",
    },
{
    "slug": "como-estas",
    "tipo": "frase",
    "titulo": "Frase: ¿Cómo estás?",
    "media": "img/frase_como_estas.gif",
    "opciones": ["¿Cómo estás?", "Gracias", "Bienvenido"],
    "respuesta": "¿Cómo estás?",
},
{
    "slug": "caminar",
    "tipo": "palabra",
    "titulo": "Palabra: Caminar",
    "media": "img/Caminar.gif",
    "opciones": ["Caminar", "Agua", "Casa"],
    "respuesta": "Caminar",
},
{
    "slug": "trabajo",
    "tipo": "palabra",
    "titulo": "Palabra: Trabajo",
    "media": "img/Trabajo.gif",
    "opciones": ["Amigo", "Trabajo", "Casa"],
    "respuesta": "Trabajo",
},
{
    "slug": "ayudar",
    "tipo": "palabra",
    "titulo": "Palabra: Ayudar",
    "media": "img/Ayudar.gif",
    "opciones": ["Casa", "Escuela", "Ayudar"],
    "respuesta": "Ayudar",
},
]

def mini_juego(request):
    # Selecciona 10 preguntas aleatorias
    preguntas = random.sample(QUIZ_ITEMS, min(10, len(QUIZ_ITEMS)))
    return render(request, 'core/mini_juego.html', {
        "titulo": "Mini juego de memoria",
        "preguntas": preguntas,
    })

# Lista de todas las letras del alfabeto (útil para el índice)
ALFABETO = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Vista 1: Muestra el índice (la lista de enlaces A, B, C...)
def alfabeto_view(request):
    contexto = {
        'titulo_pagina': 'Índice del Alfabeto',
        'letras': ALFABETO, # Enviamos la lista completa al template
    }
    # ¡Aquí le decimos que use el template que acabas de crear!
    return render(request, 'core/alfabeto_index.html', contexto)



# Vista 2: Muestra el detalle de una seña (la imagen)
def detalle_seña_view(request, letra):
    # Asegúrate de que esta extensión coincida con tus archivos (ej: A.jpg)
    ruta_imagen = f"img/{letra}.jpg"
    
    contexto = {
        'letra': letra,
        'ruta_imagen': ruta_imagen,
        'titulo_pagina': f"Seña de la Letra {letra}"
    }
    
    return render(request, 'core/detalle_seña.html', contexto)

#para los numeros

def numeros_view(request):
    titulo_pagina = "Números en Lengua de Señas"
    username = getattr(request.user, "username", "Invitado")
    numeros = list(range(1, 11))  # 1 al 10
    return render(request, "core/numeros.html", {
        "titulo_pagina": titulo_pagina,
        "username": username,
        "numeros": numeros
    })

def numeros_senal_view(request, numero):
    titulo_pagina = "Detalle del número"
    username = getattr(request.user, "username", "Invitado")
    # Ajustamos la ruta para que coincida con tus archivos .png
    ruta_imagen = f"img/numeros/numero{numero}.png"
    return render(request, "core/numeros_senal.html", {
        "titulo_pagina": titulo_pagina,
        "username": username,
        "numero": numero,
        "ruta_imagen": ruta_imagen
    })