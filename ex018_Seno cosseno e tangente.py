from math import radians, sin, cos, tan
b = int(input('Informe um angulo: '))
a = radians(b)
print('-' * 30)
print("Seno = {:.2f}\nCoseno = {:.2f}\nTangente = {:.2f}".format(sin(a),cos(a),tan(a)))