"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views            #le cambio los nombres con as ya que se llaman de igual forma el archivo views en cada app
from portfolio import views  as portfolio_views #renombro views con as, a traves del alias. 
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),  #agrego este para q sin poner nada me lleve a home
    path('home/', core_views.home, name="home"), #cambio views.home por core_views.home
    path('about-me/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),    #dentro de la app portfolio creo una carpeta templates y ahi guardo mi platilla portfolio.html, por lo tanto, aca cambio la ruta (no es en core)
    path('contact/', core_views.contact, name="contact"),
    path('contacta/', core_views.contacta, name="contacta"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static  #impoto toda la parte estatica de core/static (css, img, y demas)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #al array le agrego cosas estaticas