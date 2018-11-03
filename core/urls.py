from django.urls import path,include
from .views import index,formulario,page
urlpatterns = [ 
   path('', index,name="index"),
   path('formulario.html',formulario,name="formulario"),
   path('page.html',page,name="page")
]
