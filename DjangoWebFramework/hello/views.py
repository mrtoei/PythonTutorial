from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
   template=loader.get_template('index.php')
   user={
       'name':'Arkkarachat',
       'age': 27,
       'food':['soda','apple','water']
   }
   return HttpResponse(template.render(user,request))

