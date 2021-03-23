# Chipax Rick and Morty coding test

Este repositorio contiene la prueba de codigo de Chipax

## Meta

Generar una app MVC. Donde se ocupe el formato de las preguntas hechas por Chipax, y tener un boton
para que ocpando Ajax y asyncio se generen los calculos necesarios para obtener las respuestas a tiempo real.

Al mismo tiempo tener un script para tener las respuestas en la terminal. Todo esto bajo TDD.

## Solución (historia)

En esta prueba ocupe django para generar la solución, ya que me gusta trabajar con python y django ofrece facilidades para generar la solución final que me propuse.

Ocupe un enfoque de TDD, generando los archivos de prueba con sus respectivas "firmas" primero.

Empeze por las querys hacia RaM/Graphql, ya que no había trabajado antes con esta tecnología. 

Segui por generar los metodos que iban a interactuar con los resultados de las querys.

Luego genere el cliente y arme las soluciones de manera sincronica, como el tiempo de ejecución fue mayor al esperado, pase a ocupar asyncio para generar las soluciones a las preguntas planteadas.

Arme el script asociado a dichas preguntas, para tener la respuesta en la terminal 

Finalmente arme la vista final que se comunica con el cliente a travez del controlador para otorgar las respuestas en tiempo real.
Ocupe bootstrap para el estilo de esta pagina.
 
## Instalación

```
Git clone https://github.com/LeFranck/RaMGraphqlDjango.git
```

Añadir archivo .env

## Ejecución

Si se tienen todas las librerias es llegar y correr 
```python
  from scripts.models import raMClient
  raMClient.RaMClient.run_first_round(raMClient.RaMClient)
  raMClient.RaMClient.run_second_round(raMClient.RaMClient)
```

Si esto no funciona, apareceran en consola las librerias faltantes

Las cuales deben ser instaladas con 
```python
pip install <library>
```

Para correr los tests y vereficar que toda funciona bien basta correr
```
Python3 manage.py test /scripts
```

Falta la coordinación con las vistas debido a una falta de coordinación entre asyncio y el thread de Django
