import json

datos = '{"nombre":"Daniel", "edad":34, "pais":"España", "ciudad":"Madrid", "mascota":"Perro"}'

y = json.loads(datos)

print(y["nombre"])