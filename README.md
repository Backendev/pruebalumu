**Prueba para backend LUMU**

**CONTADOR DE FRECUENCIA DE PALABRAS**

**-Objetivo**

Saber con qué frecuencia aparece una palabra en una oración o bloque de texto es útil para

varios tipos de análisis de palabras.

Usando su lenguaje/marco preferido, cree una aplicación web que exponga

un punto final donde puede cargar un archivo de texto y devuelve como respuesta un

histograma que detalla las palabras y sus frecuencias.

**-Ejemplo:**

lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries

lumu illuminates all attacks and adversaries

**-Salida esperada:**

[

`    `{"word": "lumu","count": 6},

`    `{"word": "illuminates","count": 3},

`    `{"word": "and",”count": 2},

`    `{"word": "adversaries","count": 2},

`    `{"word": "attacks","count": 2},

`    `{"word": "all","count": 1}

]

**-Se desarrolla la solución usando:**

**Lenguaje:** Python 3.8.10

Framework para endpoint Api : FastApi = 0.75.0

**Estrategia:**

Crear un punto de acceso para diferentes generadores los cuales proporcionan 3 soluciones con enfoques diferentes y testear varios sets de datos con tamaños exponenciales para ver como se comportan cada una de las soluciones planteadas, las 3 soluciones se plantean de la siguiente manera:

**-1:** Ciclo condicional en donde se eliminen todos los elementos de la lista que coincidan con el primer elemento de esta, creando una nueva, usando una compresión de listas.

Complejidad algorítmica: n²

**-2:** Ciclo condicional en donde se convierte la lista de elementos en una cadena de texto y se usa la técnica de tokenizacion para hallar las coincidencias por medio de expresiones regulares y crear una lista nueva sin los elementos coincidentes por cada palabra

Complejidad algorítmica: n²

**-3:** Uso de pandas para tratar la lista de elementos como un dataframe e implementar los métodos de filtro para la búsqueda y la generación de el conjunto de elementos para próximas iteraciones

Complejidad algorítmica: n²

**-Metodo de ordenamiento usado para el resultado final:**

**Quicksort:** Este método fue creado por el científico británico Charles Antony Richard Hoare, tambien conocido como Tony Hoare en 1960

Se elige un elemento v de la lista L de elementos al que se le llama pivote.

Se particiona la lista L en tres listas:

L1 - que contiene todos los elementos de L menos v que sean menores o iguales que v

L2 - que contiene a v

L3 - que contiene todos los elementos de L menos v que sean mayores o iguales que v

Se aplica la recursión sobre L1 y L3

Se unen todas las soluciones que darán forma final a la lista L finalmente ordenada. Como L1 y L3 están ya ordenados, lo único que tenemos que hacer es concatenar L1, L2 y L3

Complejidad algoritmica: n log n


**-Pruebas de velocidad:**

Se desarrolla un pequeño modulo, en el que se puedan implementar cada una de las 3 soluciones sobre varias cantidades de entradas para poder visualizar el comportamiento de cada solucion y su relacion Tiempo y Cantidad de entradas



**-Mapa de proyecto**

pruebalumu

├── complexity\_analisys.py  - Modulo para ejecutar las pruebas de tiempo y cantidad de entradas de cada solución

├── config.py  - Modulo para configurar la aplicación        

├── data.py – Modulo para tratamiento de datos y contiene la función de ordenamiento                  

├── generators.py – Modulo donde se encuentran los generadores con las 3 soluciones planteadas

├── grafication.py – Modulo de apoyo a complexity\_analisys.py para graficar los resultados de este   

├── main.py – modulo principal, punto de entrada para ejecutar  la aplicación                    

├── requirements.txt – documento con requerimientos, para clonar el entorno virtual para la ejecución de la aplicación

├── time\_inputs\_all\_modes\_10000.png – grafica con 10000 entradas sobre las 3 soluciones

├── time\_inputs\_all\_modes\_1000.png – grafica con 1000 entradas sobre las 3 soluciones

├── time\_inputs\_all\_modes\_100.png – grafica con 100 entradas sobre las 3 soluciones

├── time\_inputs\_all\_modes\_10.png – grafica con 10 entradas sobre las 3 soluciones

├── time\_inputs\_all\_modes.png – Grafica temporal para visualizar los resultados de complexity\_analisys.py 

├── time\_inputs\_foreach\_modes.png – Grafica temporal para visualizar los resultados de complexity\_analisys.py 

├── time\_inputs\_foreach\_modes\_10000.png – grafica con 10000 entradas sobre las 3 soluciones

├── time\_inputs\_foreach\_modes\_1000.png – grafica con 1000 entradas sobre las 3 soluciones

├── time\_inputs\_foreach\_modes\_100.png – grafica con 100 entradas sobre las 3 soluciones

└── time\_inputs\_foreach\_modes\_10.png – grafica con 10 entradas sobre las 3 soluciones


**Como usar:**

**Crear Entorno virtual para ejecución**

**Unix -MacOs**

Crear Entorno
```
python3 -m venv env
```


Activar entorno:
```
source env/bin/activate
```

Instalar dependencias
```
python -m pip install -r requirements.txt
```
**Windows**

Crear Entorno

```
py -m venv env
```
Activar entorno:
```
.\env\Scripts\activate
```
Instalar dependencias
```
py -m pip install -r requirements.txt
```


**-🛠️Configuracion:**

en el modulo config.py puede encontrar el constructor de la Clase Config(): en el cual puede editar el puerto y el host sobre los cuales va a correr la aplicación:
```
class Config():
    def __init__(self):
        self.host = "localhost" #Ingresar direccion sin protocolo
        self.port = 3000

```






**-💻Servir la aplicación:**
```
python main.py
```
Con esto la aplicación quedara a la escucha 

**-Metodos y rutas:**

Solo se tiene la ruta raiz “/” y acepta solo el metodo POST


**-📄Enviar datos:**

Se puede usar algún servicio como Postman o hacer una petición curl al host y al puerto configurados por defecto es:

[http://localhost:3000](http://localhost:3000)

**Parametros aceptados:**

-data(str) : las palabras que se van a buscar cada una separada por un espacio de la otra

-mode(int)[1-2-3] : el numero de la solución que se va probar se aceptan 1,2 o 3 -Este parametro es opcional si no se envia se tomara por defecto el modo 1 (mas rapido en pruebas)-


puede consultar esta documentación en la ruta /docs por defecto

[http://localhost:3000/docs](http://localhost:3000/docs)

El endpoint debe devolver una lista de diccionarios con los resultados de cada palabra y la cantidad de coincidencias encontradas en el texto enviado


**📊Ejecutar pruebas de relacion tiempo-Cantidad de entradas**

En este modulo se envia una cantidad de casos que seran palabras generadas de manera aleatoria con una cantidad aleatoria de repeticiones dentro de un texto, cada una separada por un espacio

Tambien se envia una cantidad de iteraciones, que sera el numero de veces que se ejecuten esta cantidad de casos sobre las 3 soluciones, en cada iteracion se volveran a generar nuevamente la cantidad de casos configurados

El tiempo se calcula promediando todas las iteraciones y este se ira a comparar con la cantidad de casos que se configuraron

El resultado sera exportado en 2 graficas:

**1-time\_inputs\_all\_modes.png** – Grafica lineal en donde se comparan los tiempos de ejecucion y la cantidad de entradas de todos los procesos superpuestos entre si, para visualizar el comportamiento de todas las soluciones sobre la misma metrica temporal



**2-time\_inputs\_foreach\_modes.png** – Grafica lineal con cada solucion por separado y una tabla con el tiempo maximo, promedio y minimo alcanzado


**🚀Ejecutar:**
```
python  complexity_analisys.py -c *cantidad de casos* -i *cantidad de iteraciones*
```
```
python  complexity_analisys.py --cases *cantidad de casos* --iter *cantidad de iteraciones*
```

**Ejemplo:**

```
python  complexity_analisys.py --cases 50 --iter 10
```

**Nota**
La solucion modo 1 fue la que mejores resultados obtuvo y es la que se deja por defecto si no se envia parametro mode en la petición
