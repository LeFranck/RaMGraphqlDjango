# Chipax Rick and Morty coding test

Este repositorio contiene la prueba de código de Chipax

## Meta

Generar una app MVC. Donde se ocupe el formato de las preguntas hechas por Chipax, y tener un botón
para que ocupando Ajax y asyncio se generen los calculos necesarios para obtener las respuestas a tiempo real.

Al mismo tiempo tener un script para tener las respuestas en la terminal. Todo esto bajo TDD.

## Solución (historia)

En esta prueba ocupe django para generar la solución, ya que me gusta trabajar con python y django ofrece facilidades para generar la solución final que me propuse.

Ocupe un enfoque de TDD, generando los archivos de prueba con sus respectivas "firmas" primero.

Inicie por las querys hacia RaM/Graphql, ya que no había trabajado antes con esta tecnología. 

Seguí por generar los metodos que iban a interactuar con los resultados de las querys.

Luego genere el cliente y arme las soluciones de manera sincrónica, como el tiempo de ejecución fue mayor al esperado, pase a ocupar asyncio para generar las soluciones a las preguntas planteadas.

Arme el script asociado a dichas preguntas, para tener la respuesta en la terminal.

Finalmente arme la vista final que se comunica con el cliente a traves del controlador para otorgar las respuestas en tiempo real.
Ocupando Jquery agregue las respuestas obtenidas al Html sin necesidad de cambiar de pagina.

Deje la segunda respuesta (en formato api, con los id de los capítulos y origins) como un endpoint aparte en scripts/round_2/api
Ambas respuestas pueden ser consumida como API ocupando scripts/round_1/ y scripts/round_2/ respectivamente.

Ocupe bootstrap para darle estilo a la solución final.  

 
## Instalación

```
git clone https://github.com/LeFranck/RaMGraphqlDjango.git
```

Añadir archivo .env

```
pip install -r requirements.txt
```

## Ejecución

### MVC

```python
python3 manage.py runserver
```
Ingresar a http://127.0.0.1:8000/scripts/

### API
```python
python3 manage.py runserver
```

```

curl http://127.0.0.1:8000/scripts/round_1/
curl http://127.0.0.1:8000/scripts/round_2/
curl http://127.0.0.1:8000/scripts/round_2/api/
```

### Para la terminal 
```
python3
```

```python
from scripts.models import RaMClient
round_1 = RaMClient.run_first_round_console(RaMClient)
round_2 = RaMClient.run_second_round_console(RaMClient)
print(round_1)
print(round_2)
```
### Testing

Para correr los tests y vereficar que toda funciona bien basta correr
```
python3 manage.py test scripts/
```
