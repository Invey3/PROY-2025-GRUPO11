# PROY-2025-GRUPO11
Repositorio del grupo 11 del ramo Proyecto Inicial 2025

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol          |
| ----------------- | -------------- | ------------------------ | ------------ |
| Sofia Briones | @sofiabriones1      | sbriones@usm.cl | 202530019-2 |
| Felix Barrera | @felixbarrea123      | fbarrerav@usm.cl | 202530044-3 |
| Benjamin Hernandez | @bhernandezg06      | bhernandezg@usm.cl | 202530045-1 |
| Ignacio Bastías | @ibastiasm      | ibastias@usm.cl | 202530005-2 |
| Victoria Alejandra Arredondo | @victtoriaalejandra      | varredondo@usm.cl | 202304027-4 |
---

## 📝 Descripción breve del proyecto

> *Nuestro proyecto trata de un calendario menstrual de sobremesa que permita realizar un correcto seguimiento del ciclo menstrual del usuario y entregar consejos para lograr sobrellevar este proceso de manera más amigable.*

---

## 🎯 Objetivos

- Objetivo general:
  - *Crear un dispositivo de sobremesa que realice un seguimiento del ciclo menstrual del usuario.*
- Objetivos específicos:
  - Programar una interfaz amigable para el usuario.
  - Conectar de manera correcta los componentes electrónicos adicionales a las Raspberry Pico.
  - Creación de la mascota "Zuri" con sus respectivos sprites y consejos.
  - Utilizar una API de ingreso libre que nos permita tener un seguimiento a tiempo real.

---

## 🧩 Alcance del proyecto

> *Debido a las características del proyecto, el alcance del proyecto sería de carácter universal, lo cual hace que sea masivo.*

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje(s) de programación:
  - Ej: MicroPython
- Microcontroladores
  - Raspberry Pi Pico W 2
  - Pantalla LED de 5 pulgadas
  - Botones

---

## 🗂️ Estructura del repositorio

```
/PROY-2025-GRUPOX
│
├── docs/               # Documentación general y reportes https://usmcl-my.sharepoint.com/:p:/r/personal/fbarrerav_usm_cl/Documents/Presentation.pptx?d=w896cfc724f94407d805537c0e7dd8ac3&csf=1&web=1&e=pbQvMH
├── src/                # Código fuente del proyecto
├── tests/              # Casos de prueba
├── assets/             # Imágenes, diagramas, etc.
└── README.md           # Este archivo
```

---

## 🧪 Metodología

> Cascada. Hemos ido planificando y siguiendo los pasos que corresponden sin desarrollar otro antes de terminar el objetivo anterior, tales como ha sido idear el proyecto, buscar sus funciones, crear un modelo y comenzar a construirlo.

---

## 📅 Cronograma de trabajo
[PPT Ideas de trabajo](https://usmcl-my.sharepoint.com/:p:/r/personal/fbarrerav_usm_cl/Documents/Presentation.pptx?d=w896cfc724f94407d805537c0e7dd8ac3&csf=1&web=1&e=7NhVeC)

[Carta Gantt](https://www.canva.com/design/DAGl8yzWOQU/XSp1lUQktS29H-8-N6rCGA/edit?utm_content=DAGl8yzWOQU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


---

## 📚 Bibliografía

- Consejos Zuri
  - [medlineplus.org](https://medlineplus.gov/spanish/periodpain.html)
  - [corachan.com](https://www.corachan.com/es/blog/5-claves-para-aliviar-el-dolor-menstrual_138941)
  - [accuna.es](https://www.accuna.es/blog/10-consejos-para-aliviar-el-dolor-y-las-molestias-menstruales/)
  - [quironsalud.com](https://www.quironsalud.com/blogs/es/objetivo-peso-saludable/comer-regla-evitar-dolores)

---

## 📌 Notas adicionales
 Acta de reuniones:
 
 [Semana 1- Felix  e Ignacio](https://usmcl-my.sharepoint.com/:w:/r/personal/ibastias_usm_cl/Documents/Document.docx?d=wdc2e009554aa44fbbc51d711b3119999&csf=1&web=1&e=2eTX2p)
 
 [Semana 2- Sofia y Benjamin](https://usmcl-my.sharepoint.com/:w:/r/personal/bhernandezg_usm_cl/_layouts/15/Doc.aspx?sourcedoc=%7BAB17D1E9-66F8-4A3C-AB1B-1D78B4726D9C%7D&file=Consejos%20de%20Zuri.docx&action=default&mobileredirect=true&DefaultItemOpen=1)

 [Semana 3- Ignacio, Felix, Sofia y Benjamin](https://usmcl-my.sharepoint.com/:w:/r/personal/bhernandezg_usm_cl/Documents/Avance%2009-05-2025.docx?d=w0500a98a581a45eba419e0f90ef65ffa&csf=1&web=1&e=whpXBC)

 [Semana 5- Ignacio](https://usmcl-my.sharepoint.com/:w:/g/personal/ibastias_usm_cl/EXWgK4xpySxMjfPkhSu__RgBL6v4sAvtH_nLVat6FSwOIg?e=40eUHm)

 ## 📌 Codigo🤖
 
 Librerias:
 [Main.py] Funcion prindipal (Utiliza todas las librerias asi que al momento de ejecutar el programa en thonny asegurense de que estén corriendo el main.py), en cualquier caso de que en futuras actualizaciones no funcione tenemos el backup subido el 27/05, QUE UTILIZA LAS LIBRERIAS LCD_API Y PICO_I2C_LCD ESTÁS LIBRERIAS SE VAN A BORRAR EN LA ACTUALIZACION FINAL.

 
[lcd_api , pico_i2c_lcd] Funcion que se usa para limpiar la pantalla de la pantalla 16X2, estas librerias están subidas como un backup en caso de que la pantalla que debería llegar en junio esté dañada y tengamos que utilizarla como una solución parche.


[ssd1306] Esta libreria es de las más importantes. Arregló el bug de la pantalla con puntos blancos, ya que utilizaremos la pantalla oled de 128x32 para dar consejos esta libreria NO deberia ser tocada. Añadanla al Thonny y dejenla correr, lo demás no se toca.


 

 

