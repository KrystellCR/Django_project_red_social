"""platzigram views"""
#django
from django.http import HttpResponse
from django.http import JsonResponse
#utilites 
from datetime import datetime
import json

#todas las vistas reciben uun objeto requests y regresa una respuesta
def hello_world(request):
	now = datetime.now().strftime('%b %dth %Y - %H:%M hrs') #objeto por eso usamos format para mostrarlo en un string 
	return HttpResponse('Oh,hi Current server time is {now}'.format(
		now=now)) 
	#regresamos una instancia de la clase 
	#httpresponse con el contenido que nosotros queramos
	
	
def sort_integers(request):
	x= request.GET['numbers']
	import pdb;pdb.set_trace() #utilidad de python pdb es un debuger lo que hace es poner un debuger en la consola cada vez
	#que se ejecute este codigo 

	
	""" convierte el string a entero en la lista de strings llamada numbers y """
	"""  split es para convertir los string en una lista """
	numbers = [int(i) for i in request.GET['numbers'].split(',')] 
	sorted_ints= sorted(numbers)
	#diccionario data
	data = {
		'status':'ok',
		'numbers':sorted_ints,
		'message':'Integers successfuly'
	}
	
	#import pdb;pdb.set_trace()#parar la ejecucion del programa hasta que nostros le demos ctrl c
	#el metodo dumps traudce un diccionaio a un json y el parametro indent es opcional para agregar indentacion
	return HttpResponse (
		json.dumps(data,indent=4),
		content_type='application/json'
	)
	
def say_hi(request,name,age): #se le recibe el objeto request y sus argumentos 
	"""RETURN A GREETING """
	#age ya s un entero debido que ya usamos un pathconver en el archivo url
	if age <12:
		message = 'sorry {} you are not allowed here'.format(name)
		
	else:
		message='ola {} welcome to platzigram'.format(name)
	
	return HttpResponse (message)