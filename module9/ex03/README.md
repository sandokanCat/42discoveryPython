# 42 Barcelona | Discovery Piscine

## 🇬🇧 Module9 - Python

| Exercise 03: | *People Worth Knowing* |
|:-|:-|
| Turn-in directory: | **ex03/** |
| Files to turn in: | **persons_of_interest.py** |
| Allowed functions: | **All** |

- Create a program called **persons_of_interest.py**.
- This script should contain a method called **famous_births**.
- This method should take a dictionary as a parameter, representing historical figures. Each entry in the dictionary is itself a dictionary with the keys: `name` and
`date_of_birth`.
- The method should sort the dictionary by birth dates and then display each entry (see the example below).
- For example, the following script:

```python
# your method definition here

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
```

Will produce the following output:

```shell
?> ./persons_of_interest.py
Ada Lovelace is a great scientist born in 1815.
Lise Meitner is a great scientist born in 1878.
Cecila Payne is a great scientist born in 1900.
Grace Hopper is a great scientist born in 1906.
?>
```

> 💡 Google python dictionary & sorted.  
> 💡 You can also google the aforementioned names, they are worth learning about!  
> 💡 Python is a powerful tool, but it can also be a lot of fun! `print(chr(sum(range(ord(min(str(not())))))))`

---

<details>
<summary>🇪🇸 Español</summary>

## Módulo9 - Python

| Ejercicio 03: | *Personas que vale la pena conocer* |
|:-|:-|
| Directorio de entrega: | **ex03/** |
| Archivos a entregar: | **persons_of_interest.py** |
| Funciones autorizadas: | **Todas** |

- Crea un programa llamado **persons_of_interest.py**.
- Este script debe contener un método llamado **famous_births**.
- Este método debe tomar un diccionario como parámetro, representando figuras históricas. Cada entrada en el diccionario es, a su vez, un diccionario con las claves: `name` y `date_of_birth`.
- El método debe ordenar el diccionario por fechas de nacimiento y luego mostrar cada entrada (vea el ejemplo a continuación).
- Por ejemplo, el siguiente script:

```python
# your method definition here

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
```

Producirá la siguiente salida:

```shell
?> ./persons_of_interest.py
Ada Lovelace is a great scientist born in 1815.
Lise Meitner is a great scientist born in 1878.
Cecila Payne is a great scientist born in 1900.
Grace Hopper is a great scientist born in 1906.
?>
```

> 💡 Google python dictionary y sorted.  
> 💡 También puedes buscar los nombres mencionados anteriormente,
¡realmente vale la pena aprender sobre ellos!  
> 💡 ¡Python es una herramienta poderosa, pero también puede ser muy
divertido! `print(chr(sum(range(ord(min(str(not())))))))`

</details>
