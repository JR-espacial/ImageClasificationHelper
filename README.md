# Cows Dataset

Este dataset contiene 3125 imágenes tomadas en un corral del rancho **CAETEC**, corral en el que se encuentran regularmente vacas. El propósito de identificar si las vacas están presentes, paradas o sentadas y si la foto fue tomada en el día o en la noche, esto originalmente con el propósito de obtener información importante que repercute en la cálidad de la leche.

***Nota: las imágenes fueron tomadas en los meses de enero a marzo del 2024***

## Información Relevante

Las imágenes fueron clasificadas de la siguiente manera:

* Vaca : 781 ocurrencias
* No vaca : 748 ocurrencias
* Sentada : 1001 ocurrencias
* Parada : 172 ocurrencias
* Día : 673 ocurrencias
* Noche : 594 ocurrencias
* Ruido : 99 ocurrencias

Se considera que una imagen tiene *"ruido"* en la imagen no pueden apreciarse los detalles dentro del corral.

#### Consideraciones adicionales:
- Si hay dos o más vacas y ambas están sentadas o paradas, se clasifica como: noche/día, vaca, parada/sentada.
- Si hay dos o más vacas y difieren en estado de sentada/parada, se clasifica como: noche/día, vaca.
- Si solo hay pequeñas partes de la vaca, se clasifica como: no vaca, noche/día.

## Metodología

Para facilitar la clasificación de las imágenes, estas fueron renombradas del 0 al 3125 con la ayuda de un script.

Para poder llevar a cabo la clasificación de una forma más automatizada, se hizo uso de un *script* realizado en **Python**, una vez ejecutado, el programa se encarga de mostrar una imagen para seleccionar el tipo de características que posee.

Para evitar el error humano, se introdujo una validación, haciendo la clasificación entre dos personas.

Se dividió en batches iguales de 416 imágenes por cada dos personas y un batch más pequeño de 208 imágenes. Después de que cada pareja clasificara su batch con ayuda del *script*, se unieron todos los batches en [una carpeta de drive compartida](https://drive.google.com/drive/u/2/folders/1iic0UTqKdIAImybiaZoK1kFZWYEG48tD).

### Algoritmo

**Input requerido:** batch de imágenes.

1. Importar el batch de imágenes que debe estar en la carpeta `./batch`.

2. Crear las siguientes 7 carpetas:
   - Vaca.
   - No_vaca.
   - Día.
   - Noche.
   - Parada.
   - Sentada
   - Ruido

3. Iterar sobre un conjunto de imágenes. Para cada imagen:
   - Mostrar la imagen.
   - Preguntar al usuario la clasificación de la imagen (multiselect).
   - Meter cada imagen en la carpeta correspondiente:
     1. Vaca.
     2. No_vaca.
     3. Día.
     4. Noche.
     5. Parda.
     6. Sentada.
     7. Ruido.
   - Avanzar a la siguiente imagen.

## Fuente

Las imágenes fueron obtenidas del **CAETEC**, estas se encuentran en su *versión 1* y pertenecen al Dr. Ivo Ayala.
