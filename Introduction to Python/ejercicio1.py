#!/usr/bin/python3
# -*- coding: UTF-8 -*-

print ('Primer punto')
from math import cos
from math import sin
from math import sqrt
a=input("Escribe un número: ")
print 'Cos({}) = '.format(a),"{:6.3f}".format(cos(a))
print 'Cos({})= {:6.3f}'.format(a, cos(a))
print 'Sin(',a,') =',"{:6.3f}".format(sin(a)),'\n'

print ('Segundo punto')
a,b=input("Escribe la parte real e imaginaria de un número complejo: ")
z=complex(a,b)
print 'El cuadrado del \t módulo del número complejo es:',abs(z)*abs(z),'\n'

print ('Tercer punto')
a,b,c,d,e=input("Escribe 5 números: ")
print 'El cuadrado de',a,'es',a*a
print 'El cuadrado de',b,'es',b*b
print 'El cuadrado de',c,'es',c*c
print 'El cuadrado de',d,'es',d*d
print 'El cuadrado de',e,'es',e*e,'\n'

print a,a*a
print b,b*b
print c,c*c
print d,d*d
print e,e*e,'\n'

print ('Cuarto punto')
a=raw_input("Escribe un número: ")
print 'La raiz de',a,'es',sqrt(float(a)),'\n'

print ('Quinto punto')
a=raw_input("Escribe una palabra: ")
c=len(a)
print a[::-1]



print ('Séptimo punto')
a=raw_input("Escribe una palabra: ")
print a.upper()
