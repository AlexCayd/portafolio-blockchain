# Guía de estudio de blockchain

Preparación para el examen | Apuntes de la materia + quiz de 55 preguntas

Esta guía integra los 15 PDF de la carpeta, que suman 140 páginas, las cinco páginas web compartidas del profesor y el quiz para establecer prioridades. Incluye conceptos, ejemplos resueltos, fórmulas, comparaciones y ejercicios. Las referencias [Sxx] remiten a los PDF de clase, [Pxx] a las páginas del profesor y [Exx] a precisiones respaldadas con documentación primaria. Las páginas citadas son las páginas del PDF, contando la portada.

El cuestionario se entrega por separado, con los 55 enunciados originales y sus explicaciones. No se proporcionó una clave oficial: cuando una frase admite dos lecturas, se señala la interpretación usada y la alternativa. La prioridad propuesta se deduce del quiz; no garantiza la distribución del examen real.

## 1. Qué estudiar primero y cómo usar la guía

### 1.1 Mapa del quiz

| Bloque de estudio | Preguntas del quiz | Cantidad |
| --- | --- | --- |
| Firmas, claves, RSA, curvas, certificados y autenticación | 5-7, 10, 31-50, 52-55 | 28 |
| Hash, integridad, avalancha y colisiones | 12, 16, 22, 24, 26-28, 51 | 8 |
| Compromisos criptográficos | 21, 23, 29, 30 | 4 |
| Árboles y estructuras de datos | 3, 11, 25 | 3 |
| Fundamentos computacionales y Bitcoin | 1, 2, 4, 8, 9, 13-15, 17-20 | 12 |

**Prioridad alta:** domina los temas 2-8, especialmente qué hace cada clave, qué significa resistencia a colisiones y qué garantiza Bitcoin. Firmas y hash concentran 36 de las 55 preguntas.

**Prioridad media:** estudia minería, dificultad, halving y consenso, temas 9-11. Aparecen poco en este quiz, pero ocupan una parte importante de los apuntes y del proyecto.

**Ampliación y práctica:** sellado de tiempo, aplicaciones y simulador, temas 12-13. Los compromisos avanzados y las familias de firmas sirven para reconocer y comparar tecnologías, sin memorizar cada parámetro de cada curva.

### 1.2 Método para preguntas verdadero/falso

1. Identifica el objeto: ¿hash, clave, firma, bloque, transacción o protocolo?
2. Revisa las palabras absolutas: «nunca», «exclusivamente», «todos», «no tiene», «imposible».
3. Separa una propiedad matemática de una garantía práctica. Que existan colisiones no implica que podamos encontrarlas.
4. Distingue un ejemplo de clase de una regla del protocolo real.
5. Si es falso, escribe la frase corregida. Esa corrección demuestra que entendiste el concepto.

**Orden recomendado:** fundamentos → hash → compromiso → firma → RSA → curvas → Merkle → Bitcoin → PoW → probabilidad → consenso → sellado → aplicaciones. Al terminar cada tema, intenta responder las preguntas relacionadas sin consultar el cuestionario resuelto.

## 2. Fundamentos: seguridad, dificultad y vocabulario

**Quiz relacionado:** 1, 12, 33, 35-37, 54.

### 2.1 Qué significa computacionalmente inviable

Un problema puede tener algoritmos conocidos y, aun así, requerir demasiado tiempo o memoria para resolverse con los parámetros utilizados. Enumerar todas las claves o probar divisores de un entero son algoritmos; su existencia no vuelve viable el ataque.

| Concepto | Significado | Ejemplo |
| --- | --- | --- |
| Imposibilidad matemática | Algo no puede ocurrir bajo los supuestos del modelo | Un hash finito no puede ser inyectivo sobre todos los mensajes arbitrarios |
| Indecidibilidad | Ningún algoritmo resuelve correctamente todos los casos del problema | Problema general de la parada |
| Inviabilidad computacional | Hay procedimientos, pero su costo resulta prohibitivo | Recuperar una clave bien elegida mediante búsqueda exhaustiva |
| Seguridad computacional | Romper la propiedad requiere recursos fuera del modelo de amenaza | Vinculación de Pedersen bajo logaritmo discreto |
| Seguridad perfecta | La propiedad se sostiene incluso contra cómputo ilimitado | Ocultamiento de Pedersen con aleatoriedad uniforme |

En criptografía, «imposible» suele abreviar «inviable con los recursos y ataques considerados». La dificultad de factorizar números grandes no está demostrada como una imposibilidad absoluta. [S08, pp. 3-8; S10]

### 2.2 Propiedades que no debes confundir

| Propiedad | Pregunta que responde | Mecanismo típico |
| --- | --- | --- |
| Confidencialidad | ¿Quién puede conocer el contenido? | Cifrado; controles de acceso |
| Integridad | ¿El contenido fue alterado sin autorización? | Hash con referencia confiable, MAC o firma |
| Autenticidad | ¿Quién originó o autorizó el mensaje? | Firma o MAC, según el modelo |
| Autenticación de entidad | ¿El interlocutor controla la identidad o clave esperada ahora? | Reto firmado + asociación confiable de clave |
| No repudio | ¿Existe evidencia atribuible de la firma? | Firma, custodia de claves y evidencia contextual |
| Disponibilidad | ¿Se puede acceder al servicio o registro? | Replicación y diseño de red |
| Inmutabilidad práctica | ¿Qué tan difícil es reemplazar la historia aceptada? | Encadenamiento + consenso + recursos económicos |

**Integridad no significa que modificar un archivo sea físicamente imposible.** Significa conservar su corrección y poder detectar alteraciones mediante el mecanismo correspondiente. Un hash suelto no autentica: si el atacante cambia el archivo y el hash publicado, la comparación no protege. [S14, pp. 1-2]

### 2.3 Primitiva, esquema, protocolo y aplicación

- **Primitiva:** herramienta criptográfica básica; por ejemplo, hash, firma o compromiso, según el nivel de abstracción.
- **Esquema:** algoritmos y reglas que implementan una funcionalidad. Un esquema de firma especifica generar claves, firmar y verificar.
- **Protocolo:** interacción entre participantes; por ejemplo, comprometer un bit, recibir el bit del otro y revelar.
- **Aplicación:** sistema que combina estas piezas para resolver una necesidad; por ejemplo, una subasta o Bitcoin.

No existe una jerarquía universal «primitiva → protocolo → esquema como producto final». Un protocolo puede usar varios esquemas. Los propios apuntes llaman a los compromisos tanto esquema como primitiva. [S08, p. 3; S03, p. 3]

**Debes poder explicar:** por qué «no hay algoritmo» no es la definición de seguridad criptográfica; por qué integridad y confidencialidad son distintas; cómo una firma forma parte de un protocolo de autenticación.

## 3. Funciones hash: propiedades y ataques

**Quiz relacionado:** 12, 16, 22, 24, 26-28, 51, 52.

### 3.1 Qué hace un hash

Una función hash criptográfica transforma bytes de longitud variable en una huella de longitud fija:

```text
H: {0,1}* → {0,1}^n
h = H(M)
SHA-256: n = 256 bits = 32 bytes = 64 caracteres hexadecimales
```

Es determinista: los mismos bytes producen el mismo hash. Una letra acentuada, un espacio, un salto de línea o una codificación distinta pueden cambiar esos bytes. Hash no es cifrado: no hay una clave para «deshashear» y recuperar un mensaje único. [S14, p. 1]

### 3.2 Las tres resistencias

| Propiedad | Qué recibe el atacante | Qué intenta encontrar |
| --- | --- | --- |
| Preimagen | Un valor h | Un M tal que H(M) = h |
| Segunda preimagen | Un mensaje M | Otro M' distinto con H(M') = H(M) |
| Colisiones | Libertad para elegir ambos mensajes | M y M' distintos con el mismo hash |

Para un hash ideal de n bits, los costos genéricos clásicos son aproximadamente 2^n para preimagen y segunda preimagen, y 2^(n/2) para colisiones por el efecto cumpleaños. Son órdenes de trabajo, no garantías de que cualquier función con n bits alcance esa seguridad.

En SHA-256, esto corresponde idealmente a unos 256 bits frente a preimagen y 128 frente a colisiones. **256 bits de salida no significa 256 bits de seguridad frente a todo ataque.**

### 3.3 Por qué siempre existen colisiones

Los mensajes posibles son más numerosos que las 2^n salidas. Por el principio del palomar, diferentes entradas comparten salida. «Resistente a colisiones» significa que encontrarlas es difícil, no que no existan.

Por eso las preguntas «SHA-256 no tiene colisiones» y «SHA-3 no tiene colisiones» son falsas. Una función de juguete H(x) = x mod 10 lo ilustra: H(12) = H(22), pero encontrar esa colisión es trivial. Un hash criptográfico busca que esta tarea sea inviable. [S14; S08, p. 6]

### 3.4 Efecto avalancha

Cambiar un bit de la entrada debería modificar aproximadamente la mitad de los bits de salida, en promedio. En una salida de 256 bits esperamos cerca de 128 diferencias. No se exige exactamente 128 en cada comparación, ni cambiar todos los bits, ni conservarlos todos. La avalancha por sí sola tampoco demuestra resistencia a colisiones. [S07, pp. 2-3]

**Ejemplo reproducible:** SHA-256 de los bytes ASCII `hola` y `Hola` difiere en 138 de sus 256 bits. La diferencia de entrada es un solo bit: h y H tienen códigos 0x68 y 0x48.

```python
import hashlib
a = hashlib.sha256(b"hola").digest()
b = hashlib.sha256(b"Hola").digest()
distancia = sum((x ^ y).bit_count() for x, y in zip(a, b))
```

El resultado anterior se verificó ejecutando el ejemplo; no se usan como mediciones los hashes ilustrativos del apunte artesanal.

### 3.5 Familias y usos

| Función o construcción | Qué recordar |
| --- | --- |
| SHA-256 / SHA-2 | Bitcoin usa doble SHA-256 en cabeceras y en el árbol de transacciones |
| SHA-3 | Familia basada en Keccak, distinta de SHA-2; no es el hash de PoW de Bitcoin |
| BLAKE2 | Familia criptográfica; no es un ejemplo de hash roto por colisiones |
| MD5 | Tiene ataques prácticos de colisión; inadecuado para firmas o compromisos que dependan de esa resistencia |
| RIPEMD-160 | Se combina con SHA-256 en HASH160 para ciertos formatos de Bitcoin |
| HMAC | Construcción de autenticación con hash y clave secreta; no es una firma pública |
| Argon2, bcrypt, PBKDF2 | Derivación para contraseñas: añaden sal y costo; un SHA-256 rápido no basta |

La inseguridad de MD5 para usos que requieren resistencia a colisiones está documentada en [RFC 6151](https://datatracker.ietf.org/doc/html/rfc6151). [E05]

**Aplicaciones de clase:** comprobar descargas, firmar documentos y código, identificar contenido, construir Merkle, derivar claves, sellar tiempo y realizar PoW. Para contraseñas se requieren construcciones adecuadas al ataque de diccionario. [S14, pp. 1-3]

**Debes poder explicar:** preimagen frente a colisión; por qué hash no cifra; por qué el checksum debe llegar por un canal confiable; qué cambia al alterar un bit.

### 3.6 Cumpleaños, extensión de longitud y HMAC

Con k muestras de un hash ideal de n bits, la probabilidad aproximada de una colisión es:

```text
P(colisión) ≈ 1 - exp(-k(k-1) / 2^(n+1))
P ≈ 50% cuando k ≈ 1.1774 · 2^(n/2)
```

En SHA-256, conocer el digest y la longitud permite continuar el cálculo sobre un mensaje extendido que incluye el relleno correcto. Esto no recupera el texto original ni es un ataque de colisión. Puede romper un autenticador improvisado H(clave || mensaje). HMAC usa dos capas y una clave normalizada para evitar ese problema:

```text
HMAC(K,M) = H((K' XOR opad) || H((K' XOR ipad) || M))
```

La sal pública evita reutilizar trabajo entre contraseñas; no vuelve fuerte una contraseña fácil. El r de un compromiso se mantiene secreto hasta abrir y sirve a otro propósito. [P01, módulos 3, 4 y 6; E16]

**Matriz de consecuencias:** una colisión puede permitir sustituir documentos en sistemas que firman la huella; recuperar preimágenes puede revelar secretos de baja entropía; una debilidad del MAC permite alterar mensajes autenticados. Un ataque a una propiedad no demuestra automáticamente que todas las otras propiedades estén rotas. [P01, módulo 9]

### 3.7 SHA-256 por dentro

Secuencia de procesamiento: mensaje → relleno → bloques → expansión de palabras → compresión → digest. Trabaja con bloques de 512 bits, palabras de 32 bits, ocho palabras de estado y 64 rondas por bloque.

Para longitud original L, añade un bit 1, k ceros y L codificado en 64 bits; L+1+k ≡ 448 mod 512. Un mensaje de 24 bits requiere k = 423 y ocupa un bloque al añadir los 64 bits finales. El bloque se interpreta como 16 palabras, expandidas a 64:

```text
σ0(x) = ROTR7(x) XOR ROTR18(x) XOR SHR3(x)
σ1(x) = ROTR17(x) XOR ROTR19(x) XOR SHR10(x)
W[t] = σ1(W[t-2]) + W[t-7] + σ0(W[t-15]) + W[t-16]
```

Las sumas se reducen módulo 2^32. Rotar conserva los bits que salen por un extremo; desplazar introduce ceros. [P02]

La compresión utiliza las funciones Choose y Majority, rotaciones grandes y constantes de ronda:

```text
Ch(x,y,z) = (x AND y) XOR ((NOT x) AND z)
Maj(x,y,z) = (x AND y) XOR (x AND z) XOR (y AND z)
Σ0(x) = ROTR2(x) XOR ROTR13(x) XOR ROTR22(x)
Σ1(x) = ROTR6(x) XOR ROTR11(x) XOR ROTR25(x)
T1 = h + Σ1(e) + Ch(e,f,g) + Kt + Wt
T2 = Σ0(a) + Maj(a,b,c)
(a,b,c,d,e,f,g,h) ← (T1+T2,a,b,c,d+T1,e,f,g)
```

Las ocho asignaciones son simultáneas y las sumas son modulares. Al terminar las rondas, se suma el estado de trabajo al estado previo del bloque; se repite para los demás bloques y se concatenan las ocho palabras finales. [E14, §§ 5-6]

**Vector de comprobación:** SHA-256 de los tres bytes ASCII `abc` es:

```text
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

Recuerda 512, 32, 8, 64 y 256; no necesitas memorizar las 64 constantes para comprender el proceso.

## 4. Esquemas de compromiso: fijar hoy, revelar después

**Quiz relacionado:** 21, 23, 29, 30.

### 4.1 Las dos fases y las dos garantías

Un compromiso funciona como un sobre sellado: fija un valor sin mostrarlo. El esquema permite después abrirlo y verificar que coincide con lo comprometido.

```text
Setup → parámetros públicos
Comprometer: c = Com(m; r)
Abrir: comunicar m y r
Verificar: Ver(c, m, r) = 1
```

- **Ocultamiento / hiding:** el receptor no descubre el mensaje a partir del compromiso.
- **Vinculación / binding:** el emisor no puede abrir el mismo compromiso como dos mensajes diferentes.
- **Corrección:** una apertura honesta se acepta.

La fase de apertura forma parte del esquema aunque una aplicación decida no abrir ciertos compromisos. «El secreto nunca se revela» no describe el esquema general. No existe un compromiso a mensajes no triviales simultáneamente perfectamente ocultante y perfectamente vinculante en el modelo estándar de los apuntes. [S08, pp. 3-4]

### 4.2 Compromiso con hash

```text
c = H(encode(contexto, m, r))
r = aleatoriedad secreta, fresca y de suficiente entropía
Apertura: (m, r); comprobar el hash y el contexto
```

`encode` debe ser inequívoco: concatenar `ab` con `c` no debe confundirse con `a` y `bc`. El contexto puede incluir la sesión, la subasta y la identidad del participante.

Si el voto es 0 o 1 y publicas c = H(voto), el receptor calcula solo dos hashes y descubre el voto. Usar SHA-256 no corrige un espacio de mensajes minúsculo. En cambio, un r secreto y aleatorio dificulta enumerar los candidatos; los apuntes proponen al menos 128 bits de aleatoriedad. Si publicas r junto con c antes de la apertura, pierdes esa protección para mensajes pequeños. [S08, pp. 6-7]

**Fuerza bruta:** siempre puede plantearse una búsqueda exhaustiva sobre un dominio finito. Su viabilidad depende del esquema, la entropía y los parámetros. El compromiso c normalmente ya es público; lo que se busca es el mensaje o una apertura alternativa. En Pedersen perfectamente ocultante, ni el cómputo ilimitado permite identificar un único mensaje a partir de c.

**Colisiones:** en un compromiso por hash, encontrar dos aperturas a mensajes distintos con el mismo hash rompe la vinculación. Esto no significa que todos los compromisos dependan de una función hash para su binding.

### 4.3 Pedersen

En un grupo de orden primo q, con generadores g y h y sin conocer log_g(h):

```text
C = g^m · h^r
C1 · C2 = Com(m1 + m2; r1 + r2)
```

Tiene ocultamiento perfecto, vinculación computacional bajo logaritmo discreto y homomorfía aditiva. La distribución de h^r oculta m cuando r es uniforme. La homomorfía permite verificar relaciones de suma entre montos ocultos.

Si alguien conoce α con h = g^α, puede modificar la apertura: elegir r' para que m + αr = m' + αr' módulo q. Por eso la relación entre generadores debe ser desconocida. Tampoco se debe reutilizar r: dividir compromisos revela una relación entre los mensajes. [S08, p. 7]

Una ecuación de conservación modular no basta para dinero confidencial: se necesitan **pruebas de rango** para impedir valores fuera del rango permitido. Bulletproofs cumple esa función en construcciones de los apuntes; es una prueba, no una firma. [S03, p. 4]

### 4.4 Reconocimiento de construcciones avanzadas

| Construcción | Idea que debes reconocer | Propiedad o uso distintivo |
| --- | --- | --- |
| Blum | Comprometer un bit para lanzar una moneda a distancia | Protocolo commit-reveal |
| Naor | Compromiso a partir de un generador pseudoaleatorio | Ocultamiento computacional y binding estadístico |
| Hash con r | Huella del mensaje y aleatoriedad | Simple; requiere buen hash y buena codificación |
| Pedersen | Producto de potencias en un grupo | Oculta perfectamente y permite sumar |
| ElGamal como compromiso | Par (g^r, g^m h^r) | Binding perfecto; ocultamiento bajo DDH |
| Orden desconocido / RSA | Operaciones en grupos de orden oculto | Relaciones sobre enteros y credenciales |
| Merkle | Raíz que compromete un conjunto o vector | Pruebas de inclusión logarítmicas; no oculta automáticamente |
| KZG | Compromiso a un polinomio mediante emparejamientos | Aperturas pequeñas; configuración estructurada confiable |
| IPA / Bulletproofs | Argumentos de producto interno | Sin ceremonia confiable; usa grupos y compromisos |
| FRI + Merkle | Pruebas de bajo grado apoyadas en hashes | Base de STARK; configuración transparente |
| Reticulares | Problemas como SIS o Module-SIS/LWE | Alternativas para seguridad poscuántica |
| Hash camaleónico | Una trampa permite modificar aperturas | Binding depende de quién conoce la trampa |

Los KZG básicos y las raíces de Merkle no son ocultantes por definición: se necesitan variantes o aleatoriedad cuando se requiere hiding. FRI es un protocolo de prueba de proximidad que se integra en compromisos polinomiales; no debe confundirse con un hash. [S08, pp. 9-16]

### 4.5 Aplicaciones y falla del último en revelar

Subastas fijan ofertas antes de mostrarlas; preregistros fijan hipótesis; dinero confidencial verifica conservación sin publicar montos; registros de certificados prueban inclusión; custodia distribuida verifica participaciones de un secreto. [S03]

En una moneda compartida, Alice compromete a, Bob anuncia b, Alice abre y ambos usan a XOR b. El compromiso evita que Alice cambie a, pero no evita que abandone el protocolo cuando el resultado no le conviene. En aleatoriedad pública, el último en revelar puede sesgar el resultado reteniendo su aporte. **Seguridad del esquema y seguridad del protocolo son preguntas distintas.** [S03, p. 13]

## 5. Firmas digitales, identidad y certificados

**Quiz relacionado:** 10, 31, 34, 36, 40-50, 52, 54, 55.

### 5.1 El esquema de firma

```text
KeyGen() → (sk, pk)
Sign(sk, M) → firma σ
Verify(pk, M, σ) → acepta / rechaza
```

La **clave privada sk firma** y debe mantenerse secreta. La **clave pública pk verifica** y puede divulgarse. Están relacionadas matemáticamente, pero obtener sk desde pk debe ser inviable con parámetros correctos.

Una firma válida liga un mensaje con una clave. Alterar los bytes firmados hace que la firma deje de verificar. Conocer pk permite comprobar firmas, no producirlas sobre mensajes nuevos, salvo que se rompa la seguridad del esquema. [S07; S10; S12]

**Matiz sobre verificar con la privada:** las claves privadas de muchas bibliotecas contienen o permiten derivar pk, de modo que su poseedor también puede verificar. La formulación de examen «privada para firmar, pública para verificar» describe los roles de los algoritmos, no una incapacidad del dueño de sk.

### 5.2 Firma, cifrado, hash y MAC

| Herramienta | Usa secreto | Verificación pública | Oculta el mensaje | Función principal |
| --- | --- | --- | --- | --- |
| Hash | No | Se puede recalcular | No | Huella e integridad con referencia confiable |
| MAC / HMAC | Sí, compartido | No | No | Integridad y autenticidad entre quienes comparten clave |
| Firma digital | Sí, privada del firmante | Sí | No | Autorización y evidencia de origen |
| Cifrado | Sí, según el esquema | No es su propósito | Sí | Confidencialidad |
| Compromiso | Suele usar aleatoriedad secreta | Se verifica la apertura | Oculta el valor hasta apertura, si es hiding | Fijar un dato sin exponerlo |

Una firma no cifra el documento. Un mensaje firmado puede quedar visible. Un MAC no da la misma evidencia de autoría ante terceros porque cualquiera que conozca la clave compartida puede generarlo. [S14; S08]

### 5.3 Qué se firma y por qué importa el hash

En esquemas como RSA-PSS se calcula un resumen y se aplica una codificación definida por el estándar antes de la operación RSA. En ECDSA se utiliza un representante del hash. En EdDSA, el algoritmo incorpora hashes del mensaje y otros valores internamente. La aplicación no debe inventar un prehash y asumir que cualquier biblioteca lo espera.

Si un hash vulnerable permite crear dos documentos distintos con la misma huella, una firma sobre esa huella puede respaldar ambos. La seguridad exige un esquema correcto, hash apropiado, parámetros adecuados, aleatoriedad cuando corresponda y protección de sk. La clave pública además debe ser auténtica: reemplazarla por la del atacante engaña al verificador. [S14, p. 1; S10]

### 5.4 Autenticación e identidad

Firmar «acepto pagar 50» prueba autorización bajo una clave. Para probar que Bob participa ahora, el verificador puede enviar un reto fresco; Bob firma el reto con contexto y el verificador comprueba la firma. La frescura evita reutilizar una firma antigua.

Una clave por sí sola no demuestra el nombre civil del dueño. Se necesita una asociación confiable: certificado, registro previamente validado u otro modelo de identidad. En Bitcoin basta satisfacer la condición de gasto; no se exige un certificado de identidad civil para cada transacción. [E04; E07]

### 5.5 Certificados X.509

Un certificado vincula una identidad o nombre con una clave pública y lleva la firma de un emisor. X.509 no es un formato exclusivamente para guardar claves privadas.

Al verificar un certificado se revisan la firma del emisor, la cadena hasta una raíz confiable, vigencia, nombre esperado, usos permitidos y estado de revocación según el sistema. El certificado no debe revelar la clave privada del sujeto. [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280). [E04]

**Reconocimiento legal:** existen marcos jurídicos que reconocen ciertas firmas electrónicas. En la Unión Europea, las firmas electrónicas cualificadas tienen el efecto legal de una firma manuscrita; no toda firma criptográfica adquiere automáticamente esa categoría. [Comisión Europea](https://eidas.ec.europa.eu/efda/assets/i18n/home/static-html/faq/esignatures_en.html). [E06]

**Debes poder explicar:** qué prueba una firma; por qué no da confidencialidad; cómo evitar replay en autenticación; por qué no repudio requiere contexto y custodia de la clave.

## 6. RSA: claves, factorización y ejemplo resuelto

**Quiz relacionado:** 5-7, 32, 35, 39, 46, 52.

### 6.1 Construcción de las claves

Para el modelo didáctico con dos primos grandes distintos:

```text
p, q: primos secretos
n = p · q: módulo público
φ(n) = (p - 1)(q - 1)
e: exponente público, coprimo con φ(n)
d: inverso de e módulo φ(n)
e · d ≡ 1 mod φ(n)
Clave pública: (n, e)
Clave privada: (n, d), con p y q frecuentemente guardados para optimizar
```

También puede definirse d mediante λ(n), el mínimo común múltiplo de p-1 y q-1. Para el examen importa reconocer qué se publica y qué se protege. **n no es la clave privada**: está en la pública. **p y q no son la pública**: conocerlos permite reconstruir la información privada.

La seguridad se apoya en la dificultad de ataques sobre RSA; factorizar n permite calcular d. No se debe afirmar que romper cualquier esquema RSA sea un problema demostrado equivalente a factorizar: también importan el padding y la implementación. [S10; ampliación matemática]

### 6.2 Ejemplo de juguete

Elige p = 61, q = 53. Entonces n = 3233 y φ(n) = 3120. Toma e = 17 y d = 2753, pues 17 · 2753 = 46801 = 15 · 3120 + 1.

```text
Pública: (3233, 17)
Privada: (3233, 2753)
Representante del mensaje: m = 65
RSA didáctico para firma: s = 65^2753 mod 3233 = 588
Verificación didáctica: 588^17 mod 3233 = 65
```

Estos números son pequeños y el RSA «sin padding» es inseguro. El ejemplo solo muestra la relación entre exponentes; una firma real utiliza un esquema como RSA-PSS. RSA también admite esquemas de cifrado, como RSA-OAEP. La firma y el cifrado no son operaciones intercambiables.

**Proceso moderno del profesor:** hash del documento → codificación PSS con sal y MGF1 → operación privada RSA → firma. Al verificar se recupera y comprueba la codificación, junto con el mensaje. Con RSA-2048 la firma ocupa 256 bytes; con RSA-3072, 384. Dos firmas PSS del mismo documento y clave pueden diferir por la sal aleatoria. PEM/Base64 representa datos; no cifra por sí mismo una clave. [P03]

La página introductoria usa la analogía «cifrar con la privada» para RSA. Debe entenderse como intuición de la operación modular; los esquemas reales de firma y cifrado tienen codificaciones y objetivos distintos. [P04; P03]

### 6.3 Longitud y nivel de seguridad

RSA de 1024 bits no es una elección segura para generar nuevas firmas conforme a los criterios modernos citados. El tamaño se refiere al módulo n, no al número de bits del exponente e. La norma FIPS 186-5 exige módulos de al menos 2048 bits para su generación RSA. [E08]

| Seguridad clásica aproximada | Módulo RSA | Orden de grupo de curva elíptica |
| --- | --- | --- |
| 112 bits | 2048 bits | 224-255 bits |
| 128 bits | 3072 bits | 256-383 bits |

Son equivalencias orientativas del marco NIST SP 800-57, no una afirmación de que todas las curvas o implementaciones sean igual de seguras. [E09, tabla 2]

**Trampas del quiz:** Bitcoin no firma exclusivamente con RSA; p y q son secretos; RSA no sirve solo para firmas; una función hash «libre de colisiones» significa aquí resistente, no sin colisiones matemáticas.

## 7. Logaritmo discreto, curvas y familias de firmas

**Quiz relacionado:** 32, 37, 38, 53.

### 7.1 Logaritmo discreto

En un grupo cíclico G generado por g, dado y = g^x, el problema consiste en encontrar x, módulo el orden del grupo cuando este es finito. Está definido en cualquier grupo cíclico; **no es difícil en todos ellos**. La seguridad exige elegir grupos, tamaños y representaciones adecuados.

En una curva elíptica se usa notación aditiva: dado Q = dG, recuperar d es el problema del logaritmo discreto elíptico. Multiplicar el punto por d es eficiente; recuperar d debe ser inviable. [S08, p. 7; S10-S12]

### 7.2 Comparación de firmas

| Familia | Base matemática | Qué recordar |
| --- | --- | --- |
| RSA | Problema RSA; factorizar el módulo rompe la clave | Claves más grandes; esquemas de firma y cifrado distintos |
| DSA | Logaritmo discreto en un grupo finito | Firma con parámetro efímero por mensaje |
| ECDSA | Logaritmo discreto en curvas | Claves menores para seguridad comparable; Bitcoin y Ethereum de ejecución |
| EdDSA | Construcción tipo Schnorr sobre curvas Edwards | Ed25519 / Ed448; nonce derivado determinísticamente |
| Schnorr | Logaritmo discreto | Estructura lineal; Bitcoin Taproot; protocolos MuSig |
| BLS | Grupos con emparejamientos | Firmas agregables; útil en consenso |
| Basadas en hash | Seguridad de funciones hash | Familias para firma poscuántica |
| Basadas en retículas | Problemas de retículas | Alternativas poscuánticas |

La tabla de clase presenta DSA como estándar histórico y Dilithium como finalista. No debes memorizar esas etiquetas como estatus vigente: FIPS 186-5 conserva DSA para verificar firmas previas, no para generar nuevas dentro del estándar. Para el quiz basta reconocer sus fundamentos. [S10; E08]

### 7.3 El nonce de firma

En ECDSA, usando n como orden del subgrupo:

```text
Q = dG
R = kG; r = coordenada_x(R) mod n
s = k^(-1) · (z + r·d) mod n
z: representante del hash del mensaje
```

Reutilizar k en dos mensajes puede revelar d. Un k sesgado, pequeño o expuesto también puede romper la clave. Por eso se emplea generación segura o una derivación determinista adecuada. El nonce de firma es sensible: no es el contador público de minería.

En EdDSA estándar, el valor efímero se deriva de material secreto y del mensaje; no se elige una muestra aleatoria independiente para cada firma. La generación de la clave sí necesita aleatoriedad. [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032). [E03]

### 7.4 Curvas que debes reconocer

| Curva o familia | Asociación útil para estudiar |
| --- | --- |
| secp256k1 | Bitcoin: ECDSA y Schnorr; ecuación y^2 = x^3 + 7 en su campo |
| edwards25519 | Ed25519; ejemplos de clase: Cardano, Solana y Stellar |
| BLS12-381 | Firmas BLS y construcciones con emparejamientos; consenso de Ethereum |
| BN254 | Operaciones de emparejamiento para algunas pruebas en EVM |
| Jubjub / BabyJubJub | Curvas útiles dentro de circuitos de conocimiento cero |

Una curva no es un algoritmo de firma. ECDSA y Schnorr pueden compartir secp256k1. Bitcoin usa firmas Schnorr de BIP-340 en Taproot además de ECDSA en otras condiciones de gasto. [S11-S12; BIP-340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki). [E02]

### 7.5 Firmas especiales y pruebas

- **Multifirma:** requiere varias autorizaciones; MuSig2 permite producir una firma conjunta compacta bajo una clave agregada.
- **Umbral t de n:** participantes cooperan con fragmentos de una clave; no todos necesitan estar presentes.
- **Agregación:** combina firmas para reducir tamaño o costo de verificación, según el esquema.
- **Anillo:** oculta qué miembro del conjunto firmó; las variantes enlazables pueden ayudar a impedir doble gasto.
- **Grupo:** anonimato de miembros con mecanismos especiales de administración o apertura, según el sistema.
- **Ciega:** el emisor firma un mensaje sin conocer su contenido completo; útil en dinero electrónico.
- **Prueba de conocimiento cero:** demuestra una afirmación sin revelar el testigo. Bulletproofs, SNARK y STARK son pruebas; no equivalen a firmas digitales.

Estos nombres resuelven problemas distintos: autorización, privacidad del firmante, custodia distribuida o prueba de validez. [S10-S12]

### 7.6 Reconocer las verificaciones matemáticas

En ECDSA, tras validar rangos y parámetros, el verificador calcula:

```text
w = s^(-1) mod n
u1 = z·w mod n; u2 = r·w mod n
X = u1·G + u2·Q
Aceptar si X no es el punto infinito y coordenada_x(X) mod n = r
```

Una firma Schnorr conceptual satisface sG = R + eQ, donde e es un desafío hash que liga los datos pertinentes. Ed25519 sigue una relación de este tipo y deriva el valor efímero de un prefijo secreto y del mensaje. Las bibliotecas deben aplicar todas las reglas de codificación y grupo, además de la ecuación. [P03; E03]

## 8. Merkle y otras estructuras de datos

**Quiz relacionado:** 3, 11, 25.

### 8.1 Construcción de un árbol de Merkle

Para cuatro transacciones, sea h_i la huella de cada una:

```text
h1 = H(tx1)              h2 = H(tx2)
h3 = H(tx3)              h4 = H(tx4)
a  = H(h1 || h2)         b  = H(h3 || h4)
R  = H(a || b)
```

R resume y compromete el conjunto ordenado. Si cambia una transacción, cambian su hoja, sus ancestros y la raíz, con probabilidad abrumadora bajo el supuesto del hash. Construir el árbol cuesta O(N); una prueba de inclusión en un árbol equilibrado requiere O(log N) hashes. [S08, p. 9]

### 8.2 Prueba de inclusión

Para demostrar que tx3 pertenece al árbol de cuatro hojas, envía h4 y a, además de la posición u orientación de los enlaces:

```text
Calcular h3 desde tx3
Calcular b = H(h3 || h4)
Calcular R' = H(a || b)
Aceptar si R' coincide con la raíz confiable R
```

La raíz debe estar autenticada o anclada en una cadena válida. Una prueba bajo una raíz inventada no demuestra pertenencia al registro esperado. Tampoco demuestra por sí sola que la transacción sea económicamente válida o que el dato físico sea verdadero.

### 8.3 Cantidades impares y Bitcoin

No se exige que el número de transacciones sea potencia de dos. Bitcoin duplica el último hash de una fila cuando hay un número impar de elementos, y repite el procedimiento hasta obtener la raíz. Con tres hojas:

```text
a = H(h1 || h2)
b = H(h3 || h3)
R = H(a || b)
```

Duplicar un hash para construir el árbol no añade otra transacción real. En Bitcoin, H para estos pares es doble SHA-256. El txid de coinbase ocupa la primera posición. [S08; especificación de bloques](https://developer.bitcoin.org/reference/block_chain.html). [E01]

La duplicación introduce sutilezas de ambigüedad de estructura; un diseño genérico debe fijar longitud, orden y codificación y distinguir hojas de nodos cuando corresponda. La resistencia a colisiones no sustituye esas reglas. [S03, p. 16]

### 8.4 Qué estructura corresponde a qué problema

| Estructura | Función principal | Relación con la materia |
| --- | --- | --- |
| Merkle | Resumir datos y probar inclusión | Árbol de transacciones de Bitcoin |
| Patricia / trie | Buscar por prefijos con caminos comprimidos | Merkle-Patricia en diseños de Ethereum |
| Fenwick | Sumas de prefijos y actualizaciones eficientes | No es el árbol de transacciones de Bitcoin |
| Lista enlazada por hashes | Vincular un bloque con el anterior | Encadenamiento de blockchain |
| Tabla hash | Acceso por clave | Estructura auxiliar; no es una prueba Merkle |
| DAG | Grafo dirigido sin ciclos | Representación usada en otras arquitecturas; no es consenso por sí mismo |
| Verkle | Árbol con compromisos vectoriales en nodos | Pruebas de estado compactas; no confundir con Merkle |

El mapa de algoritmos enumera herramientas de todo el ecosistema; no significa que Bitcoin utilice cada una. [S02; S08, p. 9]

## 9. Bitcoin: red, transacciones y doble gasto

**Quiz relacionado:** 2, 4, 8-11, 13-20, 32, 48, 55.

### 9.1 Ideas esenciales

Bitcoin fue propuesto bajo el nombre Satoshi Nakamoto en 2008 y la red comenzó en 2009. Su innovación monetaria central combina un registro público, reglas de validación y PoW para resolver el doble gasto sin un banco central. Existieron sistemas de dinero digital anteriores; presentarlo como «la segunda moneda digital funcional» no es una clasificación histórica correcta. [S01; S09; S14]

Es una red **Peer-to-Peer**: los participantes intercambian transacciones y bloques. No tiene un servidor principal en Australia ni una autoridad central que deba comprobar cada firma. Cada nodo completo verifica las reglas por sí mismo.

**Nodo completo:** verifica y mantiene el estado según las reglas. **Minero:** construye candidatos y busca PoW. **Wallet:** administra claves y construye pagos. Una entidad puede desempeñar varios roles, pero no todos los nodos minan. [S09, pp. 1-3]

### 9.2 Seudonimato y anonimato

Bitcoin no exige un registro de identidad civil para participar; eso no garantiza anonimato. Las transacciones públicas pueden enlazarse y la información de red puede asociarse a participantes. Dirección, clave pública y nombre de una persona son objetos distintos. [Bitcoin: privacidad](https://bitcoin.org/en/protect-your-privacy). [E10]

La pregunta «los nodos son anónimos» es ambigua: puede referirse a ausencia de identificación obligatoria, o a una garantía de anonimato. Solo la primera interpretación es defendible como afirmación general de diseño.

### 9.3 UTXO y transacción firmada

Bitcoin utiliza salidas no gastadas, o UTXO. Una entrada referencia una salida previa y aporta datos para cumplir su condición de gasto; una salida define monto y condiciones para gastarlo después. En gastos ordinarios protegidos por clave, una firma válida autoriza gastar, pero además deben comprobarse todas las demás reglas. [S12; documentación de transacciones](https://developer.bitcoin.org/devguide/transactions.html). [E11]

**Ejemplo:** Bob tiene un UTXO de 1 BTC. Crea una transacción que paga 0.30 BTC a Alice y devuelve 0.699 BTC de cambio. La diferencia, 0.001 BTC, es la comisión. El UTXO de 1 BTC se consume completo; el cambio es una salida nueva.

Si Bob firma otra transacción que consume ese mismo UTXO, ambas firmas pueden ser criptográficamente válidas. No pueden aceptarse ambas como gasto del mismo recurso en la historia válida. **La firma autoriza; las reglas de estado y el consenso evitan aceptar el doble gasto.**

### 9.4 Cuándo se muestra la clave pública

En P2PKH se publica primero un hash de la clave y esta se muestra al gastar. En otras condiciones, como P2PK o Taproot, se publica una clave en la salida. Por eso es falso que toda clave pública deba revelarse antes de que exista cualquier transacción. [S12; E11]

### 9.5 Cadena aceptada y reversibilidad

Una transacción obtiene su primera confirmación cuando aparece en un bloque de la cadena activa. Si su bloque tiene altura h y la punta H, tiene H - h + 1 confirmaciones.

Dos mineros pueden producir bloques rivales. Los nodos siguen la **cadena válida con mayor trabajo acumulado**; no basta contar bloques cuando tienen dificultades diferentes. Una reorganización puede sacar una transacción de la cadena activa, y esta puede volver al mempool, volver a confirmarse o quedar invalidada por un gasto en conflicto. [S04, pp. 23-25; S09, p. 2]

**Inmutabilidad práctica no es finalidad absoluta.** Más confirmaciones reducen el riesgo bajo los supuestos del modelo. No existe un botón central para «deshacer» un pago confirmado, pero sí existe la posibilidad técnica de reorg. Esta distinción es crucial para la pregunta 9.

### 9.6 Qué un atacante mayoritario puede y no puede hacer

Una mayoría de hash puede facilitar reorganizaciones, censura y doble gasto de fondos propios mediante una rama alternativa. No le permite inventar firmas de otras personas ni hacer que un nodo correcto acepte una emisión que viola sus reglas. PoW válido no convierte automáticamente en válidas las transacciones del bloque. [S04; S09]

**Otros nombres del quiz:** Monero, Cardano e IOTA son proyectos asociados a activos digitales; Azure es una plataforma de servicios de nube, no una criptomoneda de esa lista. No confundas infraestructura, moneda, algoritmo y curva.

## 10. Minería PoW, target, dificultad y halving

**Quiz relacionado:** 14, 16, 17. Tema importante en S05, S09 y el simulador.

### 10.1 Condición de PoW

```text
hash = SHA256(SHA256(cabecera))
Válido si int(hash) ≤ T
T: target, un umbral de 256 bits
Menor T → menos hashes aceptados → mayor dificultad
```

La cabecera de Bitcoin tiene versión, hash previo, raíz de Merkle, tiempo, nBits y nonce. nBits codifica el target; no es la dificultad D. El nonce de cabecera es un entero sin signo de 32 bits. Un simulador puede usar un carácter como dato variable, pero el campo real de Bitcoin tiene formato definido. Al agotar el espacio, el minero puede modificar otros datos, incluido extranonce de coinbase. [S09, pp. 2-3; E01]

La búsqueda cuesta muchos intentos y verificar la condición cuesta calcular el hash del candidato. Aun así, validar todo un bloque requiere también revisar sus transacciones y las demás reglas.

### 10.2 Probabilidad e intentos esperados

Si las salidas se modelan como uniformes entre 0 y 2^256 - 1:

```text
s = (T + 1) / 2^256
E[intentos] = 1 / s = 2^256 / (T + 1)
D = T1 / T
E[intentos] ≈ D · 2^32
E[tiempo] ≈ E[intentos] / hashes_por_segundo
```

T1 es el target de referencia de dificultad 1. Las fórmulas de expectativa no son un plazo garantizado: puedes encontrar una solución antes o después. Los intentos fallidos no «acercan» un hash al éxito. [S09, p. 2]

### 10.3 Ceros hexadecimales: simulador frente a Bitcoin

Exigir d ceros hexadecimales al inicio equivale a exigir 4d bits cero. En ese ejercicio:

```text
Probabilidad = 16^(-d)
Intentos esperados = 16^d
d = 3 → 4096 intentos
d = 4 → 65536 intentos
d = 5 → 1048576 intentos
```

Cada cero adicional multiplica por 16 el costo esperado. Bitcoin compara con un target numérico completo; dos targets con el mismo número de ceros iniciales pueden tener dificultades diferentes.

**Corrección a S05, pp. 3-4:** la relación D ≈ 16^d omite la normalización de Bitcoin. Su dificultad 1 ya corresponde aproximadamente a 2^32 = 16^8 intentos. Si se aproxima el target por un prefijo de d ceros, se obtiene D ≈ 16^(d-8), o d ≈ 8 + log_16(D). Es una aproximación de escala, no un sustituto de calcular T1/T. Con D = 1.3 × 10^14, log_16(D) ≈ 11.72; el orden total ronda 19-20 ceros efectivos, no 11.72 ceros totales.

### 10.4 Ajuste cada 2016 bloques

```text
Δt_objetivo = 2016 · 600 s = 1209600 s = 14 días
factor = limitar(Δt_real / Δt_objetivo, entre 1/4 y 4)
T_nuevo = min(T_límite, T_anterior · factor)
```

Si el periodo fue demasiado rápido, T baja y D sube. Si fue lento, T sube y D baja. En mainnet, el cálculo usa marcas de tiempo de los bloques extremos del periodo, con la conocida diferencia de 2015 intervalos medidos frente al objetivo nominal de 2016. El formato compacto también implica redondeo. [S05; implementación Bitcoin Core](https://github.com/bitcoin/bitcoin/blob/master/src/pow.cpp). [E12]

**Ejemplo:** el periodo tarda 7 días. El factor es 1/2; T se reduce aproximadamente a la mitad y D se duplica. Si tarda 28 días, T se duplica y D se reduce a la mitad, mientras no se alcance el límite máximo.

### 10.5 Halving y subsidio

Cada 210000 bloques se reduce a la mitad el **subsidio**, la parte de monedas nuevas. La recompensa total del minero incluye también las comisiones:

```text
k = floor(h / 210000)
Subsidio ideal S(h) = 50 / 2^k BTC
Recompensa total = subsidio + comisiones
Oferta ideal = 210000 · 50 · (1 + 1/2 + 1/4 + ...) = 21000000 BTC
```

El protocolo trabaja con satoshis enteros y redondeo; la serie describe el límite nominal de 21 millones. No se debe decir que el halving reduce exactamente a la mitad las comisiones o toda la recompensa. [S05, pp. 4-5]

| Altura de inicio | Subsidio de la era |
| --- | --- |
| 0 | 50 BTC |
| 210000 | 25 BTC |
| 420000 | 12.5 BTC |
| 630000 | 6.25 BTC |
| 840000 | 3.125 BTC |
| 1050000 | 1.5625 BTC |

Las alturas son reglas; las fechas futuras son estimaciones. Para h = 650000, k = 3 y S = 6.25 BTC. Para h = 900000, k = 4 y S = 3.125 BTC.

## 11. Probabilidad de minería y mecanismos de consenso

**Apuntes principales:** S04 y S09. Estudia este tema aunque el quiz se concentre en criptografía.

### 11.1 Primero identifica qué se mantiene fijo

Hay tres niveles que no deben mezclarse:

- Un **intento de hash** tiene probabilidad s de cumplir el target.
- Un **bloque encontrado** pertenece al atacante con probabilidad q, en el modelo ideal.
- Una **espera temporal** determina cuántos bloques pueden aparecer antes de detener el experimento.

Sea q la fracción atacante y p = 1-q la honesta. Supón tasas constantes, procesos independientes y las reglas del modelo de clase. La red ideal encuentra en promedio 6 bloques por hora; con q = 0.1, las tasas son λA = 0.6 y λH = 5.4. [S04, pp. 13-18]

| Pregunta | Distribución | Dato esencial |
| --- | --- | --- |
| ¿Quién encuentra el siguiente bloque? | Bernoulli(q) | Una carrera |
| ¿Cuántos del atacante entre n bloques totales? | Binomial(n,q) | n fijo; media nq |
| ¿En qué bloque total aparece el primero del atacante? | Geométrica(q) | Media 1/q, contando el éxito |
| ¿Cuántos del atacante antes del z-ésimo honesto? | Binomial negativa | z honesto fijo; media zq/p |
| ¿Cuántos del atacante en t horas? | Poisson(λA t) | t fijo; media λA t |
| ¿Cuánto tarda el primer bloque del atacante? | Exponencial(λA) | Media 1/λA |
| ¿Cuánto tarda el r-ésimo bloque? | Gamma(r,λA) | Media r/λA, parametrizada por tasa |
| ¿Cómo cambia la ventaja entre cadenas? | Caminata aleatoria | Probabilidad de alcanzar al rival |

### 11.2 Fórmulas y ejemplos breves

```text
Binomial: P(K=k) = C(n,k) q^k p^(n-k)
Geométrica: P(G=n) = p^(n-1) q
Poisson: P(N=k) = exp(-λA·t) (λA·t)^k / k!
Exponencial: P(T≤t) = 1 - exp(-λA·t)
```

Con q = 0.1, la probabilidad de exactamente dos bloques atacantes entre los próximos 10 totales es C(10,2) · 0.1^2 · 0.9^8 ≈ 0.193710. En dos horas, λA t = 1.2 y la probabilidad de exactamente dos bloques atacantes es exp(-1.2) · 1.2^2/2 ≈ 0.216860. Tener medias parecidas no hace iguales las distribuciones.

### 11.3 Alcanzar desde una desventaja fija

Si el atacante comienza exactamente z bloques atrás, su probabilidad de alcanzar el empate en una carrera ilimitada es:

```text
a(z) = (q/p)^z, si q < p
a(z) = 1, si q ≥ p
```

Para q = 0.1 y z = 6, a(6) = (1/9)^6 ≈ 0.000001882. Esta no es todavía la probabilidad completa de doble gasto: el atacante pudo minar en secreto mientras el receptor esperaba. [S04, p. 15]

### 11.4 Doble gasto mientras se esperan z confirmaciones

El receptor espera z bloques honestos. El tiempo para obtenerlos es aleatorio; durante ese tiempo el atacante produce Mz bloques:

```text
P(Mz=m) = C(m+z-1,m) p^z q^m
E[Mz] = zq/p
Var(Mz) = zq/p^2
```

En el modelo del apunte que considera éxito alcanzar el empate y q < p:

```text
P_ataque(z) = 1 - Σ[m=0..z-1] C(m+z-1,m) · (p^z q^m - p^m q^z)
```

Para q = 0.1 y z = 6, P_ataque ≈ 0.000591412 = 0.0591412%, muy superior a a(6). Son preguntas distintas, no dos respuestas contradictorias a la misma pregunta. La probabilidad de ganar realmente un empate depende de la propagación y de la estrategia; la fórmula adopta el supuesto simplificado de éxito al alcanzar. [S04, p. 18 y nota al pie]

### 11.5 Aproximación de Nakamoto y corrección

La aproximación reemplaza el tiempo aleatorio de espera por su promedio y modela M como Poisson con media zq/p. El cálculo que conserva la variabilidad usa binomial negativa. Ambos tienen la misma media, pero distinta varianza y colas. Para confirmaciones suficientemente numerosas, la aproximación puede subestimar el riesgo; no es correcto decir que lo subestima en todos los casos. [S04, pp. 18-22]

| q | z | Aproximación Poisson | Cálculo exacto del modelo |
| --- | --- | --- | --- |
| 0.10 | 1 | 0.2045873 | 0.2000000 |
| 0.10 | 6 | 0.0002428 | 0.0005914 |
| 0.10 | 10 | 0.0000012 | 0.0000079 |
| 0.30 | 10 | 0.0416605 | 0.0651067 |

Una Poisson con tiempo Gamma aleatorio produce la binomial negativa: se puede trabajar con reloj o con bloques si se respeta qué permanece aleatorio. La idea importante es **promediar los escenarios, no sustituir una variable aleatoria por su media antes de aplicar una función no lineal**.

Seis confirmaciones es una convención de aceptación de pagos, no una garantía de riesgo cero. La coinbase de Bitcoin tiene una regla distinta: maduración de 100 bloques antes de gastarse. El simulador del curso pide una recompensa disponible en h+6; esa es su regla didáctica. [S04, pp. 23-25; S13; E13]

### 11.6 Qué resuelve un mecanismo de consenso

El consenso combina reglas para producir propuestas, validarlas y acordar una historia o estado, considerando fallos y adversarios. Debe distinguirse **seguridad** (no aceptar estados contradictorios indebidamente) de **progreso** (poder seguir produciendo decisiones). Que un sistema sea PoS no determina por sí solo su velocidad ni todo su protocolo de finalidad.

| Mecanismo | Recurso o criterio | Tipo de decisión | Limitación principal |
| --- | --- | --- | --- |
| PoW | Trabajo computacional | Cadena válida con mayor trabajo | Energía, latencia y concentración de minería |
| PoS | Participación bloqueada | Selección y votos según protocolo | Concentración de stake; complejidad de incentivos |
| DPoS | Delegados elegidos | Comité reducido con turnos | Concentración en representantes |
| PBFT / BFT | Votos de participantes | Acuerdo con finalidad bajo supuestos | Comunicación y límite de fallos |
| PoA | Validadores autorizados | Producción por entidades admitidas | Confianza en admisión y autoridades |
| Espacio y tiempo | Almacenamiento y retardo | Pruebas del recurso | Hardware y concentración |
| PoET | Espera certificada | Sorteo apoyado en hardware confiable | Confianza en hardware |

PoS puede usar protocolos BFT: estas categorías no son excluyentes. En el PBFT clásico, n ≥ 3f+1 permite tolerar hasta f fallos bizantinos; con 10 participantes se toleran hasta 3 bajo sus supuestos. No significa que «exactamente un tercio malicioso siempre es seguro». [S09, pp. 11-12]

### 11.7 PoS de clase: sorteo y voto ponderado

Con garantías b_i y total S:

```text
P(proponente i) = b_i/S
Aceptar en el modelo de clase si 3V ≥ 2S
V: suma de garantías de quienes votan a favor
```

Ana tiene 3, Beto 2 y Carla 1: S = 6. Sus intervalos de sorteo son Ana {0,1,2}, Beto {3,4} y Carla {5}. Si r = 4, propone Beto. Si solo Ana y Carla votan a favor, V = 4: 3·4 = 2·6, y se acepta justo en el umbral. Si solo Ana vota, V = 3 y se rechaza.

El voto pesa por garantía, no por contar personas. Ganar el sorteo da derecho a proponer, no a imponer un bloque inválido. En la versión de juguete, el castigo por doble firma reduce garantía y expulsa; en el proyecto se pide una regla de castigo por rechazo. No todos los protocolos reales castigan cualquier bloque rechazado del mismo modo. [S09, pp. 5-9; S13]

### 11.8 Mecanismos adicionales del catálogo

| Nombre | Idea distintiva |
| --- | --- |
| Algorand | Selección de comités mediante funciones aleatorias verificables y acuerdo bizantino |
| Avalanche | Consultas aleatorias repetidas hasta convergencia con parámetros de seguridad |
| Chia | Prueba de espacio combinada con tiempo |
| Proof of History | Secuencia verificable para ordenar eventos; necesita un consenso que la acompañe |
| Hashgraph | DAG de eventos, gossip sobre gossip y voto virtual |

DAG es estructura, Proof of History aporta orden temporal y PoS define un criterio económico: ninguno de esos nombres sustituye por sí solo la descripción completa de las reglas de validación y acuerdo. [S09, pp. 13-17]

### 11.9 Generales bizantinos: acuerdo y supuestos

Una falla bizantina puede mentir, omitir mensajes o enviar versiones contradictorias. Una caída solo deja de responder. En el problema comandante-tenientes, los leales deben coincidir (**IC1**) y, si el comandante es leal, obedecer su orden (**IC2**). Si el comandante es traidor, todavía se exige IC1. [P05]

Con mensajes orales, sin prueba transferible del origen, tres generales no toleran un traidor. Un teniente que recibe «atacar» y oye «el comandante dijo retirarse» no distingue un comandante leal con otro teniente mentiroso de un comandante traidor. IC2 obliga a atacar en el primer escenario; al intercambiar los papeles, el otro leal debe retirarse. En el escenario de comandante traidor se viola IC1. El resultado depende del modelo, no de falta de ingenio. [E15, pp. 3-4]

OM(1), con cuatro generales, funciona en dos rondas: el comandante envía la orden; los tenientes comparten lo recibido y usan la misma regla de mayoría y de desempate. Para órdenes iniciales atacar/retirarse/atacar de un comandante traidor, los tres tenientes leales reciben el mismo conjunto y deciden atacar. [E15]

Para quórums de n-f nodos, dos decisiones comparten al menos n-2f. Exigir que haya un leal en el traslape da n-2f > f, es decir n > 3f. Con n = 7 y f = 2, cada quórum tiene 5, comparten al menos 3 y al menos uno es leal. [P05]

**Firmas:** SM aprovecha evidencia reenviable de quién emitió cada orden; un traidor todavía puede firmar órdenes incompatibles. Cambiar este modelo no elimina automáticamente el umbral de un tercio en PBFT o en finalidad PoS. [E15; S09]

**Sybil:** crear muchas identidades no debe equivaler a crear poder ilimitado. PoW pondera por trabajo y PoS por participación, en lugar de contar claves. **FLP:** en asincronía completa con una posible caída, un protocolo determinista no garantiza terminar el consenso en todas las ejecuciones. No afirma que siempre falle el acuerdo; limita la garantía de progreso. Los protocolos usan supuestos temporales o aleatoriedad para abordar ese límite. [P05]

**Ejercicio adicional:** con 13 validadores, ¿cuál es f máximo en el modelo n ≥ 3f+1? **Respuesta:** 4. Cinco fallos exigirían al menos 16 validadores.

## 12. Sellado de tiempo y blockchain artesanal

**Apuntes principales:** S15, S07 y S13.

### 12.1 Qué prueba un sello

Busca demostrar que un dato estaba comprometido o existía antes de un momento verificable. Cambiar la fecha de un archivo no ofrece esa evidencia.

En el esquema TSA, se envía el hash del documento a una autoridad de sellado. Esta emite un token firmado que liga huella, algoritmo, tiempo y otros campos. El verificador revisa la firma y compara la huella del documento. La confianza incluye la clave y el reloj de la autoridad. [S15, p. 1]

Enviar solo un hash no garantiza secreto para datos predecibles: un tercero puede probar candidatos. Cuando eso importa, se emplea aleatoriedad o un esquema de protección apropiado, conservando los datos de apertura.

### 12.2 Encadenamiento y Merkle

Haber-Stornetta liga registros sucesivos y publica o distribuye testigos del estado. Un árbol de Merkle agrupa muchos documentos: se ancla una raíz y cada usuario conserva su prueba de inclusión. OpenTimestamps es el ejemplo del material que ancla en Bitcoin. [S15, p. 2; S03, p. 9]

**Límite:** un anclaje no demuestra quién creó el documento ni que su contenido sea verdadero. La marca de tiempo de un bloque tampoco es un reloj civil exacto; aporta evidencia de orden y existencia bajo las reglas de la red. Un timestamp local por sí solo no equivale a un sello confiable.

### 12.3 Las cuatro piezas de la cadena artesanal

| Pieza | Qué aporta |
| --- | --- |
| Hash | Huella verificable del contenido |
| Firma | Evidencia de autorización bajo una clave |
| Hash previo | Encadenamiento con el estado anterior |
| Marca o sello temporal | Orden temporal; confianza depende de cómo se obtiene |

Un bloque artesanal puede contener índice, tiempo, transacción, hash previo, hash propio y firma. No debe introducirse el hash propio como parte de su propio cálculo. Deben fijarse todos los campos cubiertos antes de calcular el hash o la firma correspondiente. [S07, pp. 1-4]

**Orden coherente:** construir transacción → fijar índice, tiempo y hash previo → serializar sin ambigüedad → calcular el hash → firmar los bytes o el resumen que exige el esquema → ensamblar → verificar y publicar. El diagrama de S07 pone algunas piezas después de la firma, pero su pseudocódigo fija el tiempo antes del hash; este último orden es el coherente.

### 12.4 Qué verificar

1. Recalcular cada hash a partir de los campos cubiertos.
2. Verificar la firma con la clave pública correspondiente.
3. Comprobar el enlace con el bloque anterior y la altura.
4. En un libro de pagos, reproducir el estado y comprobar fondos y ausencia de doble gasto.
5. En una red distribuida, comprobar consenso y elección de rama.

Un atacante puede recalcular una cadena de hashes por sí sola. La resistencia a reescribir una historia pública necesita firmas, anclajes conocidos o consenso según el diseño. La cadena artesanal enseña la estructura criptográfica; no implementa por sí misma el consenso de Bitcoin. [S07, p. 4]

## 13. Aplicaciones y conexión con el proyecto

**Apuntes principales:** S01, S03, S06 y S13.

### 13.1 Cuándo tiene sentido usar blockchain

La pregunta inicial es si varias partes necesitan compartir un registro y no aceptan depender de un único administrador. Después se pregunta quién puede escribir, quién valida, qué amenaza se busca evitar y si bastan firmas y una base de datos convencional.

| Sector | Registro o proceso | Piezas relevantes | Límite que debes explicar |
| --- | --- | --- | --- |
| Finanzas y pagos | Transferencias, liquidación y activos tokenizados | Firma, estado y consenso | Un token no garantiza respaldo ni liquidez |
| Industria, construcción y logística | Lotes, componentes, entregas e hitos | Identidad, trazabilidad y registros compartidos | La entrada puede ser falsa o incompleta |
| Alimentos, farmacia y cadena de frío | Origen, custodia y condiciones | Sensores, firmas y auditoría | La cadena no vuelve confiable al sensor |
| Automotriz, aviación y lujo | Historial y autenticidad de piezas o bienes | Registros y vínculos con objeto físico | Puede fallar la asociación entre etiqueta y objeto |
| Salud e identidad | Credenciales, consentimiento y control de acceso | Firmas, permisos y pruebas | Privacidad y gobernanza de datos |
| Universidad, ciencia y propiedad intelectual | Títulos, preregistro y versiones | Hash, compromiso y sello temporal | Anclar no acredita por sí solo autoría o calidad |
| Gobierno y votación | Auditoría y decisiones compartidas | Compromisos y pruebas verificables | Coerción, dispositivos e identidad no se resuelven solo con blockchain |
| Turismo, deporte y medios | Lealtad, boletos, derechos y activos digitales | Tokens y contratos | Adopción y derechos externos siguen siendo necesarios |

Los PDF de aplicaciones incluyen propuestas, pilotos y sistemas desplegados en distintas fechas. Esta tabla resume las funciones de clase sin presentar cada caso empresarial como vigente. [S01; S06]

### 13.2 Contratos inteligentes y oráculos

Un contrato inteligente ejecuta reglas sobre información que la red puede procesar. No conoce automáticamente la temperatura real de una vacuna o si una obra terminó: necesita un **oráculo** o una fuente externa.

La blockchain puede demostrar que el registro «5 °C» no cambió después; no demuestra que la temperatura real haya sido 5 °C. El dato debe sustentarse con captura confiable, auditoría y responsabilidad. Tampoco la criptografía corrige un contrato con errores de lógica. [S06, p. 9]

En datos sensibles, una arquitectura habitual conserva el contenido fuera de cadena y ancla huellas o pruebas. Incluso una huella puede permitir correlación o ataques de diccionario: «solo subimos hashes» no resuelve toda la privacidad.

### 13.3 Compromisos en aplicaciones

| Necesidad | Herramienta apropiada para reconocer |
| --- | --- |
| Ocultar montos y comprobar conservación | Pedersen + pruebas de rango |
| Fijar ofertas antes de mostrarlas | Commit-reveal con nonce y contexto |
| Probar inclusión en registro de certificados | Merkle y raíz autenticada |
| Verificar fragmentos de una clave distribuida | Compromisos de coeficientes / VSS |
| Demostrar un atributo sin revelar toda la identidad | Credenciales + pruebas de conocimiento cero |
| Demostrar una evaluación polinomial | Compromiso polinomial, como KZG o IPA |
| Probar existencia previa de una hipótesis | Compromiso + sello temporal |

La selección depende de si se necesita ocultar, sumar, abrir parcialmente, evitar una ceremonia confiable o resistir ataques cuánticos. [S08, p. 16; S03]

### 13.4 Qué debes entender del simulador solicitado

No se desarrolla aquí la aplicación: esta sección explica los conceptos que la rúbrica obliga a dominar.

- **Común:** 10-20 nodos, claves, transacciones firmadas, copia de cadena por nodo y validación antes de aceptar.
- **Serialización:** los mismos campos deben producir los mismos bytes. Usar orden y codificación canónicos evita que dos nodos calculen huellas distintas de un mismo objeto lógico.
- **Estado:** fondos suficientes y control del doble gasto también dentro del mismo bloque; verificar firma no reemplaza esas comprobaciones.
- **PoW:** competencia visible; el minero i prueba i, i+N, i+2N...; se detienen al encontrar ganador; se documenta desempate.
- **Recompensa PoW:** en el proyecto, la del bloque h se acredita en h+6. Esa altura implica seis bloques posteriores; no es la maduración de coinbase de Bitcoin.
- **PoS:** bloquear apuestas válidas, sortear proporcionalmente, verificar candidatos y aceptar si 3V ≥ 2A. Una firma alterada o gasto excesivo debe producir rechazo.
- **Castigo:** seleccionar y justificar la regla de la guía del proyecto, liberar o descontar fondos correctamente y repetir el sorteo cuando corresponda.
- **Robustez:** rechazar entradas inválidas, acciones duplicadas y cadenas corruptas sin dejar saldos o estados inconsistentes.

**Diferencias de alcance:** el simulador usa SHA-256 simple, una red que puede simularse en memoria, cadena válida más larga y reglas didácticas de PoS. Bitcoin usa doble SHA-256 en PoW, red P2P real, mayor trabajo acumulado y maduración coinbase de 100 bloques. [S13; S04; S09]

La rúbrica asigna 35% a robustez, 15% a bloques/firmas/validación, 20% a PoW, 20% a PoS, 5% a interfaz y 5% a reporte/video. El archivo fija tamaño de reporte y duración del video, pero deja fecha de entrega y equipos por definir. [S13, pp. 5-6]

## 14. Repaso activo, ejercicios y glosario

### 14.1 Veinte frases que debes poder explicar

1. Seguridad computacional no significa ausencia de algoritmos.
2. SHA-256 tiene colisiones matemáticas; buscarlas debe ser difícil.
3. Avalancha significa cerca de la mitad de bits distintos en promedio.
4. Un hash no cifra y no autentica por sí solo.
5. Comprometer fija sin revelar; abrir permite comprobar.
6. Hiding protege el secreto; binding impide cambiar el mensaje comprometido.
7. H(voto) se enumera fácilmente si solo hay dos votos posibles.
8. Pedersen oculta perfectamente y vincula bajo logaritmo discreto.
9. La privada firma y la pública verifica.
10. La clave pública no debe permitir recuperar la privada eficientemente.
11. RSA publica (n,e), no sus factores p y q.
12. RSA también tiene esquemas de cifrado; firma y cifrado son diferentes.
13. Una curva no es un algoritmo de firma.
14. EdDSA estándar deriva su nonce del secreto y el mensaje.
15. Bitcoin usa Merkle, PoW y doble SHA-256; firma con ECDSA y también Schnorr.
16. Bitcoin no ofrece anonimato garantizado ni una autoridad central de validación.
17. Las firmas autorizan; el estado y el consenso controlan el doble gasto.
18. Una reorganización puede sacar un pago de la cadena activa.
19. Menor target significa mayor dificultad; el halving reduce el subsidio.
20. Un sello o registro inalterado no prueba que el contenido sea verdadero.

### 14.2 Ejercicios de comprensión

**A. Hash y firma.** Cambias «pagar 50» por «pagar 500». ¿Qué ocurre con el hash y la firma? ¿Sirve cifrar para conseguir lo mismo?

**B. Compromiso.** Una subasta publica H(oferta), y todas las ofertas son múltiplos de 100 entre 0 y 10000. ¿Cuántos candidatos puede probar un rival? ¿Qué falta?

**C. RSA.** Para p = 11, q = 13 y e = 7, calcula n, φ(n) y d. Identifica qué datos se publican.

**D. Merkle.** ¿Qué hashes adicionales necesitas para probar la inclusión de la tercera hoja de un árbol de ocho transacciones?

**E. PoW.** En el simulador se pasa de 3 a 5 ceros iniciales. ¿Por qué factor aumenta el costo esperado?

**F. Dificultad.** Un periodo nominal de 14 días tarda 10.5. ¿Qué pasa con T y D?

**G. Halving.** Calcula el subsidio en altura 1050000. ¿Se reducen a la mitad las comisiones?

**H. PoS.** Garantías 40, 30, 20 y 10. ¿Quién propone con r = 75? Si solo votan los dos primeros, ¿se acepta?

**I. Probabilidad.** Elige la distribución para: bloques atacantes en una hora; bloques atacantes antes del sexto honesto; tiempo hasta el tercero atacante.

**J. Doble gasto.** ¿Por qué una firma válida no impide que su dueño firme dos gastos del mismo UTXO?

**K. Sellado.** Una tesis se ancla mediante una raíz Merkle. ¿Qué debe conservar su autor? ¿Prueba eso que sus resultados sean correctos?

**L. Aplicación.** Dos universidades quieren compartir certificados. Explica cuándo bastarían firmas y cuándo aportaría algo un registro común con varios validadores.

### 14.3 Respuestas de los ejercicios

**A:** el hash cambia con probabilidad abrumadora y la firma deja de verificar para el mensaje modificado. Cifrar busca confidencialidad; no sustituye la firma.

**B:** hay 101 candidatos. Falta aleatoriedad secreta suficiente, codificación inequívoca y contexto de subasta.

**C:** n = 143; φ(n) = 120; d = 103, porque 7·103 = 721 ≡ 1 mod 120. Se publica (143,7); se protegen d y los factores. Sigue siendo un ejemplo inseguro de juguete.

**D:** h4; el hash del subárbol de hojas 1-2; y el hash del subárbol de hojas 5-8, con la orientación de cada paso. Son tres hashes hermanos.

**E:** 16^(5-3) = 256. El número esperado pasa de 4096 a 1048576 intentos.

**F:** el factor es 10.5/14 = 0.75. T se multiplica por 0.75 y D por 1/0.75 = 4/3, aproximadamente.

**G:** k = 5; subsidio = 50/32 = 1.5625 BTC. Las comisiones no tienen un halving automático.

**H:** intervalos [0,40), [40,70), [70,90), [90,100); propone el tercero. V = 70 y 3V = 210 ≥ 200: se acepta en el modelo, si el bloque es válido.

**I:** Poisson; binomial negativa; Gamma/Erlang, respectivamente.

**J:** ambas firmas prueban autorización bajo la misma clave. El estado permite gastar cada UTXO una sola vez y el consenso decide la historia válida.

**K:** documento exacto, prueba de inclusión y evidencia del anclaje; si hay nonce, también los datos de apertura. La prueba respalda existencia o compromiso previo, no calidad científica.

**L:** firmas bastan para acreditar emisor e integridad cuando no se necesita un estado compartido. Un registro común puede aportar acuerdo sobre emisión, revocación y actualizaciones entre partes con administración independiente; debe justificarse su gobernanza.

### 14.4 Glosario rápido

| Término | Definición breve |
| --- | --- |
| sk / pk | Clave privada / pública |
| Digest | Huella o resumen producido por hash |
| Nonce | Valor usado según un protocolo; minería, firma y compromiso le dan roles distintos |
| Sal | Valor que diversifica derivaciones de contraseñas; habitualmente se guarda junto al resultado |
| UTXO | Salida de transacción aún no gastada |
| Mempool | Conjunto local de transacciones pendientes aceptadas por un nodo |
| Coinbase | Transacción especial de recompensa de un bloque; no confundir con la empresa |
| Target | Umbral que debe cumplir el hash de PoW |
| Dificultad | Relación entre target de referencia y target actual |
| Confirmación | Inclusión en cadena activa y bloques posteriores que la respaldan |
| Reorg | Cambio de la rama activa de la cadena |
| Stake | Participación bloqueada que interviene en un protocolo PoS |
| Slashing | Penalización protocolaria por ciertas conductas demostrables |
| VRF | Función aleatoria verificable |
| VDF | Función de retardo verificable |
| TSA | Autoridad de sellado de tiempo |
| CA | Autoridad certificadora |
| Trusted setup | Configuración cuya seguridad exige condiciones de confianza específicas |
| ZK | Conocimiento cero: probar sin revelar el testigo |
| Oráculo | Fuente que introduce datos externos al sistema |

### 14.5 Plan de repaso en tres sesiones

**Sesión 1:** temas 2-7. Escribe de memoria las propiedades hash, hiding/binding, los roles de claves y las claves RSA. Resuelve los reactivos relacionados.

**Sesión 2:** temas 8-11. Construye una prueba Merkle, explica un doble gasto y resuelve ejercicios de target, halving, PoS y selección de distribuciones.

**Sesión 3:** temas 12-13 y quiz completo sin respuestas. Revisa cada error con su justificación; vuelve a resolver las preguntas ambiguas explicando qué supuesto cambia la respuesta.

**Criterio de dominio:** no solo recuerdas V/F; puedes corregir cada afirmación falsa y dar un ejemplo que distinga conceptos cercanos.

## 15. Fuentes y precisiones de lectura

Las fuentes de clase se enumeran a continuación. Se consultaron también las cinco páginas del profesor: laboratorio de hash, recorrido de SHA-256, firmas técnicas, introducción a firma y generales bizantinos. Las tablas de firma y curvas son material de reconocimiento, no una lista que deba memorizarse íntegra. Los catálogos de aplicaciones se usan para explicar mecanismos; sus estadísticas y anuncios empresariales no se presentan como verificación de actividad actual.

**Correcciones destacadas:** se preserva la diferencia entre «resistente a colisiones» y «sin colisiones»; la posibilidad de reorg se toma de S04 frente a las frases absolutas de S01/S09; la normalización de dificultad se aclara en el tema 10; subsidio y comisiones se separan; timestamps locales se distinguen de sellos confiables; y las reglas del proyecto se identifican como didácticas.

### PDF de la carpeta

**[S01]** [7_cur_19_00120Apuntes20- Copy.pdf](../../7_cur_19_00120Apuntes20-%20Copy.pdf). 22 páginas. Panorama general y aplicaciones sectoriales.

**[S02]** [8_cur_19_001_BlockChain_Algoritmos.pdf](../../8_cur_19_001_BlockChain_Algoritmos.pdf). 1 páginas. Mapa de algoritmos, estructuras y herramientas.

**[S03]** [aplicaciones_compromiso.pdf](../../aplicaciones_compromiso.pdf). 20 páginas. Usos de compromisos, privacidad, pruebas y errores de integración.

**[S04]** [apuntes_mineria_pow.pdf](../../apuntes_mineria_pow.pdf). 26 páginas. Distribuciones, confirmaciones, doble gasto y reorganizaciones.

**[S05]** [bitcoin_target_halving-1.pdf](../../bitcoin_target_halving-1.pdf). 6 páginas. Target, ajuste de dificultad y subsidio.

**[S06]** [blockchain-aplicaciones.pdf](../../blockchain-aplicaciones.pdf). 10 páginas. Aplicaciones por sector y límites de las propuestas.

**[S07]** [blockchain_artesanal.pdf](../../blockchain_artesanal.pdf). 4 páginas. Construcción y validación de una cadena artesanal.

**[S08]** [compromisos.pdf](../../compromisos.pdf). 18 páginas. Definiciones, seguridad y familias de compromisos.

**[S09]** [consenso_blockchain-1.pdf](../../consenso_blockchain-1.pdf). 17 páginas. Consenso, PoW, PoS y ejemplos de votación.

**[S10]** [cur_19_00120Apuntes20Digital Tabla.pdf](../../cur_19_00120Apuntes20Digital%20Tabla.pdf). 1 páginas. Comparación de familias de firma.

**[S11]** [cur_19_00120Apuntes20Digital20Curves BlockChain.pdf](../../cur_19_00120Apuntes20Digital20Curves%20BlockChain.pdf). 1 páginas. Curvas y grupos usados en el ecosistema.

**[S12]** [cur_19_00120Apuntes20de20Digital BlockChain.pdf](../../cur_19_00120Apuntes20de20Digital%20BlockChain.pdf). 1 páginas. Firmas y pruebas en blockchains.

**[S13]** [guia_simulador_blockchain.pdf](../../guia_simulador_blockchain.pdf). 6 páginas. Requisitos y rúbrica del simulador.

**[S14]** [hash_aplicaciones.pdf](../../hash_aplicaciones.pdf). 4 páginas. Propiedades y aplicaciones de hash.

**[S15]** [time_stamping.pdf](../../time_stamping.pdf). 3 páginas. Métodos de sellado de tiempo.

### Páginas del profesor

**[P01]** [Laboratorio de funciones hash](http://math.com.mx/funciones_hash.html).

**[P02]** [SHA-256 paso a paso](http://math.com.mx/sha256.html).

**[P03]** [Guía técnica de RSA, DSA, ECDSA y EdDSA](http://math.com.mx/firmas_digitales.html).

**[P04]** [Firma digital: de RSA a blockchain](http://math.com.mx/firma_digital.html).

**[P05]** [Generales bizantinos y acuerdo distribuido](http://math.com.mx/g_b.html).

### Documentación primaria para precisiones

**[E01]** [Bitcoin Developer Reference: cabeceras y Merkle](https://developer.bitcoin.org/reference/block_chain.html).

**[E02]** [BIP-340: firmas Schnorr sobre secp256k1](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki).

**[E03]** [RFC 8032: EdDSA](https://www.rfc-editor.org/rfc/rfc8032).

**[E04]** [RFC 5280: certificados X.509](https://www.rfc-editor.org/rfc/rfc5280).

**[E05]** [RFC 6151: seguridad de MD5](https://datatracker.ietf.org/doc/html/rfc6151).

**[E06]** [Comisión Europea: reconocimiento de firmas electrónicas](https://eidas.ec.europa.eu/efda/assets/i18n/home/static-html/faq/esignatures_en.html).

**[E07]** [NIST FIPS 186-5: finalidad de la firma digital](https://csrc.nist.gov/pubs/fips/186-5/final).

**[E08]** [FIPS 186-5: tamaños RSA y algoritmos de firma](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf).

**[E09]** [NIST SP 800-57 Parte 1 Rev. 5: tabla de seguridad comparable](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

**[E10]** [Bitcoin: privacidad de participantes](https://bitcoin.org/en/protect-your-privacy).

**[E11]** [Bitcoin Developer Guide: transacciones y P2PKH](https://developer.bitcoin.org/devguide/transactions.html).

**[E12]** [Bitcoin Core: ajuste del target](https://github.com/bitcoin/bitcoin/blob/master/src/pow.cpp).

**[E13]** [Bitcoin Core: maduración de coinbase](https://github.com/bitcoin/bitcoin/blob/master/src/consensus/consensus.h).

**[E14]** [NIST FIPS 180-4: SHA-256](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf).

**[E15]** [Lamport, Shostak y Pease: The Byzantine Generals Problem (1982)](https://lamport.azurewebsites.net/pubs/byz.pdf).

**[E16]** [RFC 2104: construcción HMAC](https://www.rfc-editor.org/rfc/rfc2104).

Consulta y preparación: 8 de octubre de 2026. Los sitios externos pueden actualizarse; los identificadores permiten localizar el fundamento concreto.
