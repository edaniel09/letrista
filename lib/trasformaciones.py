import re
import random

def aplicar_reverso(linea):
	return ''.join(reversed(linea))

def aplicar_no_vocales(linea):
	lineamod = linea
	lineamod = lineamod.replace('a', "")
	lineamod = lineamod.replace('e', "")
	lineamod = lineamod.replace('i', "")
	lineamod = lineamod.replace('o', "")
	lineamod = lineamod.replace('u', "")
	return lineamod

def aplicar_palindromo(linea):
	palabras_array = linea.split(' ')
	mod_array = []
	for palabra in palabras_array:
		longitud = len(palabra)
		palabra = palabra[0:round(longitud/2)+1]+str(''.join(reversed(palabra[0:round(longitud/2)])))
		mod_array.append(palabra)
	res =' '.join(mod_array)
	return res

def aplicar_no_consonantes(linea):
	lineamod = linea
	lineamod = lineamod.replace('b', "").replace('c', "").replace('d', "").replace('f', "").replace('g', "").replace('h', "").replace('j', "").replace('k', "").replace('l', "").replace('m', "").replace('n', "").replace('p', "").replace('q', "").replace('r', "").replace('s', "").replace('t', "").replace('v', "").replace('w', "").replace('x', "").replace('y', "").replace('z', "")
	return lineamod

def aplicar_shuffle(linea):
	array = linea.split()
	strres = ''
	for word in array:
		chars = list(word)
		random.shuffle(chars)
		word = ''.join(chars)
		strres+=(word+" ")
	return strres

def aplicar_orden_letras(linea):
	resultado = []
	coordenadas = []
	for letra in linea:
		if letra.lower() in 'aeiou':
			coordenadas.append('v')
		elif letra.lower() in 'bcdfghjkmnlpqrstvwxyzñ':
			coordenadas.append('c')
		else:
			coordenadas.append('e')
	vocales = sorted(aplicar_no_consonantes(linea).replace(' ','').lower())
	consonantes = sorted(aplicar_no_vocales(linea).replace(' ','').lower())
	pos_vocal = 0 
	pos_cons = 0
	for index in range(len(linea)):
		if coordenadas[index] == 'v':
			resultado.append(vocales[pos_vocal])
			pos_vocal+=1
		elif coordenadas[index] == 'c':
			resultado.append(consonantes[pos_cons])
			pos_cons+=1
		else:
			resultado.append(linea[index])
	res = re.sub(r'(.)\1+', r'\1', ''.join(resultado))
	return res