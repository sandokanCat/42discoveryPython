# 42 Barcelona | Discovery Piscine

## 🇬🇧 Module9 - Python

| Exercise 01: | *Family Matters* |
|:-|:-|
| Turn-in directory: | **ex01/** |
| Files to turn in: | **family_affairs.py** |
| Allowed functions: | **All** |

- Create a program called **family_affairs.py**.
- This script should contain a method called **find_the_redheads**.
- This method will take a dictionary as a parameter, where the keys are family members' first names and the values are their hair colors.
- The method should use the `filter` function to collect the first names of individuals with red hair into a new list, which it will return.
- The result must be converted into a list before being returned by using the function `list()`.
- For example, the following script:

```python
# your method definition here

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
```

Will produce the following output:

```shell
?> ./family_affairs.py
['florian', 'david', 'franck']
?>
```

> 💡 Google Python dictionary `filter`, `keys()`, `list()`.

---

<details>
<summary>🇪🇸 Español</summary>

## Módulo9 - Python

| Ejercicio 01: | *¡Organiza esta lista de nombres para mí!* |
|:-|:-|
| Directorio de entrega: | **ex01/** |
| Archivos a entregar: | **family_affairs.py** |
| Funciones autorizadas: | **Todas** |

- Crea un programa llamado **family_affairs.py**.
- Este script debe contener un método llamado **find_the_redheads**.
- Este método tomará un diccionario como parámetro, donde las claves son los nombres de los miembros de la familia y los valores son los colores de su cabello.
- El método debe usar la función `filter` para recopilar los nombres de las personas con cabello rojo en una nueva lista, que debe devolver.
- El resultado debe ser convertido en una lista antes de ser devuelto usando la función `list()`.
- Por ejemplo, el siguiente script:

```python
# your method definition here

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
```

Producirá la siguiente salida:

```shell
?> ./family_affairs.py
['florian', 'david', 'franck']
?>
```

> 💡 Busca Python dictionary `filter`, `keys()`, `list()`.

</details>
