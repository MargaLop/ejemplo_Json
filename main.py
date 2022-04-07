import json

#EJERCICIO 1

# datos = '''{"nombre":"Daniel", 
# "edad":34, 
# "pais":"España", 
# "ciudad":"Madrid", 
# "mascota":"Perro"
# }'''

# y = json.loads(datos)

# print(y["nombre"])


#EJERCICIO 2

texto = '¡¡Buenos días, mi querido usuario!!'

with open('libro.txt','w') as f:
    f.write(texto)

with open('variable.txt','r') as f:   
    mi_variable = f.read()

my_weapon = json.loads(mi_variable)

print(my_weapon['nombre'])
print(my_weapon['comida'])
print('-----------')
print(my_weapon)