# 42 Barcelona | Discovery Piscine

## 🇬🇧 Module8 - Python

| Exercise 03: | *Let’s Say Hello to everyone!* |
|:-|:-|
| Turn-in directory: | **ex03/** |
| Files to turn in: | **greetings_for_all.py** |
| Allowed functions: | **All** |

- Create a program called **greetings_for_all.py** that does not take any parameters.
- Ensure this program is executable.
- Create a method called **greetings** which takes a name as a parameter and displays a welcome message with that name.
- If the method is called without an argument, its default parameter should be `noble stranger`.
- If the method is called with an argument that is not a string, an error message should be displayed instead of the welcome message.

```shell
?> cat greetings_for_all.py | cat -e
# your method definition here

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
```

Will produce the following output:

```shell
?> ./greetings_for_all.py | cat -e
Hello, Alexandra.$
Hello, Wil.$
Hello, noble stranger.$
Error! It was not a name.$
?>
```

---

<details>
<summary>🇪🇸 Español</summary>

## Módulo8 - Python

| Ejercicio 03: | *¡Vamos a Saludar a Todos!* |
|:-|:-|
| Directorio de entrega: | **ex03/** |
| Archivos a entregar: | **greetings_for_all.py** |
| Funciones autorizadas: | **Todas** |

- Crea un programa llamado **greetings_for_all.py** que no reciba parámetros.
- Asegúrate de que este programa sea ejecutable.
- Crea un método llamado **greetings** que reciba un nombre como parámetro y muestre un mensaje de bienvenida con ese nombre.
- Si el método es llamado sin un argumento, su parámetro por defecto debe ser `noble stranger`.
- Si el método es llamado con un argumento que no sea una string, debe mostrar un mensaje de error en lugar del mensaje de bienvenida.

```shell
?> cat greetings_for_all.py | cat -e
# your method definition here

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
```

Producirá la siguiente salida:

```shell
?> ./greetings_for_all.py | cat -e
Hello, Alexandra.$
Hello, Wil.$
Hello, noble stranger.$
Error! It was not a name.$
?>
```

</details>
