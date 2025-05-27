from machine import Pin, I2C
from time import sleep, sleep_ms
import ssd1306

# --- Clase LCD 16x2 (4-bit) COMPLETA ---
class LCD:
    def __init__(self, rs=2, en=3, d4=4, d5=5, d6=6, d7=7):
        self.rs = Pin(rs, Pin.OUT)    # RS en GP2
        self.en = Pin(en, Pin.OUT)    # E en GP3
        self.data_pins = [
            Pin(d4, Pin.OUT),  # D4 en GP4
            Pin(d5, Pin.OUT),  # D5 en GP5
            Pin(d6, Pin.OUT),  # D6 en GP6
            Pin(d7, Pin.OUT)   # D7 en GP7
        ]
        self._init()  # Cambiado a _init para evitar confusión
    
    def _init(self):
        """Secuencia de inicialización del LCD"""
        self.cmd(0x33)
        sleep_ms(5)
        self.cmd(0x32)
        sleep_ms(5)
        self.cmd(0x28)  # 4 bits, 2 líneas
        self.cmd(0x0C)  # Display on, cursor off
        self.cmd(0x01)  # Clear
        sleep_ms(2)
        self.cmd(0x06)  # Increment, no shift
    
    def cmd(self, byte):
        """Envía comando al LCD"""
        self.rs(0)
        self._write_byte(byte)
    
    def _write_byte(self, byte):
        """Escribe byte en 2 partes de 4 bits"""
        # Parte alta
        for i in range(4):
            self.data_pins[i]((byte >> (i+4)) & 0x01)
        self._pulse_en()
        # Parte baja
        for i in range(4):
            self.data_pins[i]((byte >> i) & 0x01)
        self._pulse_en()
    
    def _pulse_en(self):
        """Genera pulso en Enable"""
        self.en(1)
        sleep_ms(1)
        self.en(0)
        sleep_ms(1)
    
    def putstr(self, text):
        """Escribe cadena de texto"""
        for char in text:
            self.putchar(ord(char))
    
    def putchar(self, char):
        """Escribe un carácter"""
        self.rs(1)
        self._write_byte(char)
    
    def clear(self):
        """Limpia la pantalla"""
        self.cmd(0x01)
        sleep_ms(2)
    
    def move_to(self, col, row):
        """Mueve cursor a posición (col, row)"""
        addr = col + (0x40 if row else 0x00)
        self.cmd(0x80 | addr)

# --- Configuración OLED (I2C en GP0 y GP1) ---
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# --- Configuración LCD ---
lcd = LCD(rs=2, en=3, d4=4, d5=5, d6=6, d7=7)

# --- Variables del sistema ---
inicio_ciclo_dia = 3
duracion_ciclo = 28
dias_dolor = [1, 2, 3]
dia_actual = 9
mes_actual = 5  # Mayo
anio_actual = 2025

# --- Diccionario de consejos (sin tildes) ---
consejos = {
    "Dolor menstrual": "- Descansa y usa calor\n- Analgesicos suaves\n- Evita cafeina",
    "Menstruacion": "- Hidratate bien\n- Alimentos con hierro\n- Descansa",
    "Fase fertil": "- Fertilidad alta\n- Energia elevada\n- Buen momento",
    "Fase lutea": "- Antojos comunes\n- Snacks saludables\n- Relajate"
}

# --- Funciones mejoradas ---
def formato_fecha(dia, mes, anio):
    """Devuelve fecha como DD/MM/AAAA"""
    return f"{dia:02d}/{mes:02d}/{anio}"

def calcular_dia_ciclo(dia):
    return (dia - inicio_ciclo_dia) % duracion_ciclo + 1

def evento_del_dia(dia):
    dia_ciclo = calcular_dia_ciclo(dia)
    if dia_ciclo in dias_dolor:
        return "Dolor menstrual"
    elif dia_ciclo <= 5:
        return "Menstruacion"
    elif 14 <= dia_ciclo < 19:
        return "Fase fertil"
    else:
        return "Fase lutea"

def mostrar_pantallas():
    # Calcular valores
    evento = evento_del_dia(dia_actual)
    fecha = formato_fecha(dia_actual, mes_actual, anio_actual)
    
    # Actualizar LCD
    lcd.clear()
    lcd.putstr(fecha)
    lcd.move_to(0, 1)
    lcd.putstr(evento.center(16))
    
    # Actualizar OLED
    oled.fill(0)
    oled.text("CONSEJO:", 0, 0)
    oled.hline(0, 10, 128, 1)
    for i, linea in enumerate(consejos[evento].split('\n')):
        oled.text(linea, 0, 15 + i * 10)
    oled.show()

# --- Inicialización ---
lcd.clear()
oled.fill(0)
oled.text("Sistema OK", 0, 0)
oled.show()
sleep(2)

# --- Bucle principal ---
while True:
    mostrar_pantallas()
    sleep(3)  # Cambiar a 86400 para tiempo real
    
    dia_actual += 1
    if dia_actual > 28:
        dia_actual = 1
        mes_actual += 1
        if mes_actual > 12:
            mes_actual = 1
            anio_actual += 1