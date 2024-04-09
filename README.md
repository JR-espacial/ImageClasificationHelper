# Cows Dataset

Este dataset contiene 3125 imágenes tomadas en un corral del rancho **CAETEC**, corral en el que se encuentran regularmente vacas. El propósito de identificar si las vacas están presentes, paradas o sentadas y si la foto fue tomada en el día o en la noche, esto originalmente con el propósito de obtener información importante que repercute en la cálidad de la leche.

***Nota: las imágenes fueron tomadas en los meses de enero a marzo del 2024***

## Metodología

Para facilitar la clasificación de las imágenes, estas fueron renombradas y clasificadas a través de folders. Las imágenes están nombradas del 0 al 3125

Para poder llevar a cabo la clasificación de una forma más automatizada, se hizo uso de un *script* realizado en **Python**, una vez ejecutado, el programa se encarga de mostrar una imagen para seleccionar el tipo de características que posee.

Para evitar el error humano, se introdujo una validación, haciendo la clasificación entre dos personas.

### Algoritmo

**Input requerido:** batch de imágenes

1. Importar el batch de imágenes que debe estar en la carpeta `./batch`.

2. Crear las siguientes 7 carpetas:
   - vaca.
   - no_vaca.
   - día.
   - noche.
   - parda.
   - sentada
   - Ruido

3. Iterar sobre un conjunto de imágenes. Para cada imagen:
   - Mostrar la imagen.
   - Preguntar al usuario la clasificación de la imagen (multiselect).
   - Meter cada imagen en la carpeta correspondiente:
     1. vaca.
     2. no_vaca.
     3. día.
     4. noche.
     5. parda.
     6. sentada.
     7. Ruido.
   - Avanzar a la siguiente imagen.

## Información Relevante

Las imágenes fueron clasificadas de la siguiente manera:

* Vaca.
* No vaca.
* Sentada.
* Parada.
* Día.
* Noche.
* Ruido.  

Se considera que una imagen tiene *"ruido"* en la imagen no pueden apreciarse los detalles dentro del corral.

## Fuente

Las imágenes fueron obtenidas del **CAETEC**, estas se encuentran en su *versión 1* y pertenecen al Dr. Ivo Ayala.
