# ImageClasificationHelper
## Contexto:

Estamos creando un script que nos ayude a clasificar vacas en diferentes carpetas mostrando cada imagen de una vaca para que nosotros podamos decir a qué carpeta meterla. Ayúdame a generar el script de Python que muestre de manera gráfica y pida input al usuario.


## Algoritmo:

**Input requerido:** batch de imágenes

1. Importar el batch de imágenes que debe estar en la carpeta `./batch`.

2. Crear las siguientes 7 carpetas:
   - vaca 
   - no_vaca
   - día
   - noche
   - parda 
   - sentada
   - Ruido

3. Iterar sobre un conjunto de imágenes. Para cada imagen:
   - Mostrar la imagen.
   - Preguntar al usuario la clasificación de la imagen (multiselect).
   - Meter cada imagen en la carpeta correspondiente:
     1. vaca 
     2. no_vaca
     3. día
     4. noche
     5. parda 
     6. sentada
     7. Ruido
   - Avanzar a la siguiente imagen.
