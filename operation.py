#!/usr/bin/python3

# 13.6 Calculadora

# Susana Zarzalejo Herrera

fich = open("/etc/passwd", "r")

import sys

if len(sys.argv) != 4:
	sys.exit("usage: operation.py operacion operando1 operando2")

function = sys.argv[1]
number1 = float(sys.argv[2])
number2 = float(sys.argv[3])

print('=======Welcome=======')

if function == 'suma':
	op ='+'
	sol = number1 + number2
	print(number1 ,op ,number2 , ' = ' ,sol)
elif function == 'resta':
	op='-'
	sol = number1 - number2 
	print(number1, op,number2, ' = ',sol)
elif function == 'multiplicación':
	op= '*'
	sol = number1 * number2 
	print(number1, op,number2, ' = ',sol)
elif function == 'división': 
	try: 
		sol = number1 / number2 
		op =':'
	except ZeroDivisionError: 
		print('Invalid Argument')
		op  ='can not be divided by'
		sol =' Try Again'
		print(number1, op, number2, ' = ', sol)
else: 
	print('Use this operations: suma, resta, multiplicación or división')
