# 📜 Libro I: Las Parábolas del Código

Habiendo dominado el Génesis y los fundamentos de la creación, la deidad Jesubuntu nos entregó las parábolas: ejemplos terrenales para aplicar la sabiduría divina a los problemas del día a día.

En este libro aprenderemos los milagros de la transformación de datos (casteo) y los métodos sagrados para manipular textos y listas.

---

### [Capítulo 1: La Transmutación de la Materia](./parabola_del_imc.py) (Casteo y Mates)

**Versículo 1:1 - La conversión del texto a número.** Cuando el usuario entrega su ofrenda mediante un `input()`, esta llega en forma de texto (*string*). Para realizar cálculos matemáticos terrenales (como el Índice de Masa Corporal), debemos transmutar esa ofrenda usando `float()` para números con decimales o `int()` para números enteros.

**Versículo 1:2 - El redondeo divino.** Para que los números no se extiendan hasta el infinito y saturen la mente humana, usamos `round(numero, cantidad_decimales)` para acotar su existencia.

**Versículo 1:3 - El retorno a la palabra.** Al igual que el número nace del texto, debe volver al texto para ser mostrado junto a otras palabras. Invocaremos a `str()` para convertir de vuelta el cálculo en una cadena.
`print("Tu índice de masa corporal terrenal es " + str(imc_divino) + " 🙏🏻")`

---

### Capítulo 2: Los Milagros de la Palabra (Métodos de Strings)

Los textos no son inmutables; pueden ser moldeados y purificados con los métodos sagrados.
*(Reflejado en: [`bautismo_del_correo.py`](./bautismo_del_correo.py), [`sello_de_las_iniciales.py`](./sello_de_las_iniciales.py), [`milagros_de_las_cadenas.py`](./milagros_de_las_cadenas.py), [`guardia_del_santuario.py`](./guardia_del_santuario.py))*

**Versículo 2:1 - La purificación de los espacios (`strip`).** Limpia los pecados (espacios en blanco) que sobran al principio y al final de una cadena invocando `.strip()`.

**Versículo 2:2 - La transformación de la voz (`lower` y `upper`).** - `.lower()`: Humilla la cadena, convirtiendo todo a minúsculas. Ideal para crear correos institucionales o validar contraseñas sin importar cómo escriba el usuario.
- `.upper()`: Alza la voz al cielo, convirtiendo todo a mayúsculas. Perfecto para esculpir iniciales.

**Versículo 2:3 - La coronación de las letras (`title` y `capitalize`).**
- `.capitalize()`: Corona únicamente la primera letra de toda la frase.
- `.title()`: Corona la primera letra de *cada palabra* dentro de la oración, dándole el porte de un título sagrado.

**Versículo 2:4 - El milagro de la división (`split`).** Cuando una oración es demasiado larga, `.split()` la fractura en pedazos, separando las palabras por sus espacios vacíos y creando una sagrada *Lista* con cada fragmento.

**Versículo 2:5 - El milagro de la unión (`join`).** Toma una lista de palabras dispersas y las unifica en un solo texto, entrelazándolas con el símbolo o espacio que tú elijas: `" | ".join(lista)`.

**Versículo 2:6 - La búsqueda de la verdad (`find` y `count`).**
- `.find("texto")`: Busca en la cadena y te revela la posición exacta donde nace por primera vez lo que estás buscando.
- `.count("texto")`: Cuenta cuántas veces se repite un elemento en la oración.

---

### [Capítulo 3: La Multiplicación de las Listas](./milagros_de_las_cadenas.py)

Las listas son los pergaminos donde guardamos a nuestros fieles. Así es como se gestionan:

**Versículo 3:1 - La ofrenda final (`append`).** Añade un nuevo elemento al final del pergamino, respetando el orden de llegada.

**Versículo 3:2 - La inserción profética (`insert`).** Te permite elegir la posición exacta (el índice) donde quieres colocar un nuevo elemento, desplazando a los demás con delicadeza.
`lista.insert(2, "Miércoles")`

**Versículo 3:3 - La fusión de las tribus (`extend`).** Si tienes dos listas distintas y deseas unirlas en una sola hermandad, `.extend()` absorbe los elementos de una lista y los integra en la otra.

**Versículo 3:4 - El exilio (`pop` y `del`).** Todo lo que empieza, termina. `.pop()` extrae y elimina el último elemento (o uno específico), guardando su esencia en una variable. `del` lo borra de la existencia para siempre.