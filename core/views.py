from re import template
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

"""
html_base = "" "
    <h1>Mi web personal</h1>
    <ul>
        <li><a href="/home">Portada</a></li>
        <li><a href="/about-me">Acerca de mi</a></li>
        <li><a href="/portfolio">Portafolio</a></li>
        <li><a href="/contact">Contacto</a></li>
    </ul>
"" " #es como si fuera una plantilla, pero despues lo cambio por un archivo .html y lo ertorno en cada func de abajo
"""
# Create your views here.

def home(request):
    return render(request,"core/home.html")
#    return HttpResponse(html_base + """<h2>Portada</h2>
#                        <p>Esto es una portada</p>""") (*)1 estas dos lineas las cambio por algo mejor, era solo un ejempl

def about(request):
    return render(request,"core/about-me.html")
#(*)1    return HttpResponse(html_base + """<h2>Acerca de mi</h2>
#                        <p>Me llamo Agustin y soy alumno de CaC</p>""")    #para que se vea lo tengo que agregar al path dentro de urls.py

#me llevo la vista de portfolio a su propia app (dentro de su view)
#def portfolio(request):
#    return render(request,"core/portfolio.html")
#(*)1    return HttpResponse(html_base + """<h2>Portafolio</h2>
#                        <p>Estos son algunos de mis trabajos</p>""")

def contact(request):
    return render(request,"core/contact.html")
#(*)1    return HttpResponse(html_base + """<h2>Contacto</h2>
#                        <p>e-mail: guarmes@gmail.com</p>""")

def contacta(request):
    if request.method == "POST":
        name = request.POST['txtNombre']
        email = request.POST['txtCorreo']
        message = request.POST['message']
        subject = "Se quieren contactar desde mi portafolio"
        
        template = render_to_string('core/email_template.html', {
            'name': name,
            'email': email,
            'message': message,
        })
        
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['agustinguarmes@gmail.com']
        )
        
        email.fail_silently = False     #para que no marque un error en gmail
        email.send()
        
        messages.success(request,"Correo enviado.")
        return render(request,"core/contact.html")