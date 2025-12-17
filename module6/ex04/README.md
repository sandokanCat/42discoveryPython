# 42 Barcelona | Discovery Piscine

## 🇬🇧 Module6 - Python

| Exercise 04: | *Scanning a Tex* |
|:-|:-|
| Turn-in directory: | **ex04/** |
| Files to turn in: | **scan_it.py** |
| Allowed functions: | **All** |

- Create a program called **scan_it.py**.
- Ensure this program is executable.
- This program should take two parameters.
- The first parameter is a keyword to search for in a string.
- The second parameter is the string to be searched.
- When executed, the program should display the number of times the keyword appears in the string.
- If the number of parameters is different from 2 or if the first string does not appear in the second, it should display `none` followed by a newline.

```shell
?> ./scan_it.py | cat -e
none$
?> ./scan_it.py "the" | cat -e
none$
?> ./scan_it.py "the" "hello world" | cat -e
none$
?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
2$
?>
```

> 💡 You can use the `re.findall()` method in Python's `re` module.

---

<details>
<summary>🇪🇸 Español</summary>

## Módulo6 - Python

| Ejercicio 04: | *Escanear un String* |
|:-|:-|
| Directorio de entrega: | **ex04/** |
| Archivos a entregar: | **scan_it.py** |
| Funciones autorizadas: | **Todas** |

- Crea un programa llamado **scan_it.py**.
- Asegúrate de que este programa sea ejecutable.
- Este programa debe tomar dos parámetros.
- El primer parámetro es una palabra clave para buscar en un string.
- El segundo parámetro es el string en el que se va a buscar.
- Al ejecutarse, el programa debe mostrar el número de veces que aparece la palabra clave en el string.
- Si el número de parámetros es diferente de 2 o si el primer string no aparece en el segundo, debe mostrar `none` seguido de un salto de línea.

```shell
?> ./scan_it.py | cat -e
none$
?> ./scan_it.py "the" | cat -e
none$
?> ./scan_it.py "the" "hello world" | cat -e
none$
?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
2$
?>
```

> 💡 Puedes usar el método `re.findall()` módulo `re` de Python.

</details>
