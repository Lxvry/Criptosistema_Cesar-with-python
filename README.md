# Criptosistema_Cesar-with-python

# Introduccion

El criptosistema o cifrado cesar, es un tipo de cifrado simetrico. Esto quiere decir que utiliza una misma clave tanto para cifrar como para descifrar.

Una criptografia simetrica esta formada por un conjunto de elementos los que llamamos clave o llaves, y una regla que asocia dos aplicaciones a cada clave. Vamos a darle el valor de Z por lo que diriamos z E Z.

Entonces todas las claves existentes pertenecen al conjunto Z.

de forma que: 

Funcion de cifrado

```python
cz = Mz -> Cz
```
Funcion de decifrado

```python
dz = Cz -> Mz
```
Siendo `cz` y `dz` la funcion de cifrado y decifrado.
`Mz` el mensaje en texto plano o claro.
`Cz` el mensaje cifrado. 

A menudo `Mz` es el mismo conjunto para todas las claves y asi mismo `Cz`.

##### Por ejemplo

Si tenemos que **A** es un conjunto de numeros finitos (o sea, una cantidad limitada de numeros por ejemplo {1,2,3}) y denotemos por **Pa**, un conjunto de permutaciones de los elementos de el conjunto finito **A**. ¿Que queremos decir con esto?. Nos referimos a la cantidad de combinaciones que son posibles de los elementos del conjunto **A**, por ejemplo, (3,2,1), (2,1,3),(1,3,2),(3,1,2), etc.

Sustitucion: Tomamos como conjunto de claves *Z = Pa*  como conjuntos de mensajes basicos *M = N = A* y como funciones de cifrado y descifrado:

*c(o,x) = o(x)*				y			d(o,x) = o^-1(y)

siendo o = nuestro conjunto de permutaciones **(Pa)** y x nuestro texto plano. Por lo que cifra el mensaje **(x)** usando la clave o en este caso el cifrado *c(o,x)*, el cual se encarga de aplicar la permutacion **o** a **x**, esto quiere decir que estaria reorganizando **x** segun el valor de la permutacion **o**.

mientras que **o^-1** es la permutacion que deshace o revierte, esto formaria parte de el decifrado.

## Nivel Teorico de Criptosistema o cifrado Cesar

Esto podemos usarlo de distintas formas, lo primero seria eligiendo el abecedario espanol o en su formato ingles (o bien cualquier otro idioma como frances, italiano o etc.), para elegir el numero correspondiente al modulo, agregar letras acentuadas y/o bien separando minusculas de mayusculas o elegir una sola.

Vamos a trabajar con el abecedario en ingles y solamente mayusculas, por lo cual el valor a identificar para nuestro modulo seria de 25. Este valor corresponderia al valor total de letras en el abecedario, empezando siempre la cuenta desde el 0 en adelante. (0-25).

A = 0 | B = 1 | C = 2 | D = 3 | E = 4 | F = 5 | G = 6 | H = 7 | I = 8 | J = 9 | K = 10 | L =11 | M = 12 | N =13 | O = 14 | P = 15 | Q = 16 | R = 17 | S = 18 | T = 19 | U = 20 | V = 21 | W = 22 | X = 23 | Y = 24 | Z = 25 | " space " = 26

Ponemos *Z = M = C = L26*

entonces:
		*cz(x) = (x + z mod 26)*
		*dz(x) = (x - z mod 26)*

Ahora eligimos alguna letra del abecedario, la cual sera nuestra clave y elegimos su valor numero correspondiente, por ejemplo la **I**, que tiene un valor de 8.

Cifraremos un mensaje como "Hola mundo".
#### HOLA MUNDO

*cz('mensaje') = ('Mensaje' + clave mod 26)*

**REMPLAZAMOS**
cz(x) = ('Hola mundo' + 8 mod 26)

Lo primero que habria que hacer es transformar el "Hola mundo". Quedando algo asi

####  7 14 11 0 12 20 13 3 14

Ahora a cada elemento de este le sumamos la clave `+ 8`. Si la suma entre el elemento y la clave supera o iguala el modulo este debe retornar su valor a 0 y agregarle lo sobrante, de otra forma se podria entender asi. 

Si A + B mod 26 
C = valor de la suma entre A + B
C - 26 = D
D = valor final.

25 + 8 mod 26
33 mod 26
33 - 26 = 7

Si la suma entre el elemento y la clave es menor a el modulo, se conserva simplemente igual.

Entonces el mensaje cifrado quedaria algo asi: 

#### 15 12 19 8 8 20 2 21 11 22

Paso final es la sustitucion de estos numeros por la posicion de las nuevas letras y obtendremos el mensaje cifrado

#### PWTIIUCVLW
