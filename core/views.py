from django.shortcuts import render, redirect
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
# Create your views here.
