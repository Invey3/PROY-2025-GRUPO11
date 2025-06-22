from machine import I2C
from lcd_api import LcdApi
from time import sleep_ms

class I2cLcd(LcdApi):
    """Implements a HD44780 character LCD connected via I2C."""
    
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.num_lines = num_lines
        self.num_columns = num_columns
        
        # Configuración inicial
        self.backlight = True
        self.displayfunction = 0
        self.displaycontrol = 0
        self.displaymode = 0
        
        # Inicialización
        self.init()
    
    def init(self):
        # Secuencia de inicialización específica para I2C
        self.write_cmd(0x03)
        sleep_ms(5)
        self.write_cmd(0x03)
        sleep_ms(1)
        self.write_cmd(0x03)
        sleep_ms(1)
        self.write_cmd(0x02)  # Modo 4 bits
        sleep_ms(1)
        
        # Configuración básica
        self.write_cmd(0x20 | 0x08)  # 4 bits, 2 líneas
        sleep_ms(1)
        self.write_cmd(0x08 | 0x04)  # Display On
        sleep_ms(1)
        self.clear()
        self.write_cmd(0x04 | 0x02)  # Increment, no shift
        sleep_ms(1)
    
    def write_cmd(self, cmd):
        """Escribe un comando al LCD"""
        buf = bytearray(2)
        buf[0] = 0x80 if self.backlight else 0x00
        buf[1] = cmd & 0xF0
        self.i2c.writeto(self.i2c_addr, buf)
        
        buf[1] = (cmd & 0x0F) << 4
        self.i2c.writeto(self.i2c_addr, buf)
        
        if cmd <= 3:
            sleep_ms(5)
    
    def write_data(self, data):
        """Escribe datos al LCD"""
        buf = bytearray(2)
        buf[0] = 0xC0 if self.backlight else 0x40
        buf[1] = data & 0xF0
        self.i2c.writeto(self.i2c_addr, buf)
        
        buf[1] = (data & 0x0F) << 4
        self.i2c.writeto(self.i2c_addr, buf)
    
    def clear(self):
        """Limpia la pantalla"""
        self.write_cmd(0x01)
        sleep_ms(2)
    
    def home(self):
        """Mueve el cursor a la posición inicial"""
        self.write_cmd(0x02)
        sleep_ms(2)
    
    def move_to(self, col, row):
        """Mueve el cursor a la posición especificada"""
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        if row >= self.num_lines:
            row = self.num_lines - 1
        self.write_cmd(0x80 | (col + row_offsets[row]))
    
    def putchar(self, char):
        """Escribe un caracter en la posición actual"""
        self.write_data(char)
    
    def putstr(self, string):
        """Escribe una cadena de texto"""
        for char in string:
            self.putchar(ord(char))
    
    def backlight_on(self):
        """Enciende la luz de fondo"""
        self.backlight = True
        self.i2c.writeto(self.i2c_addr, bytearray([0x08]))
    
    def backlight_off(self):
        """Apaga la luz de fondo"""
        self.backlight = False
        self.i2c.writeto(self.i2c_addr, bytearray([0x00]))
    
    def show_cursor(self, show=True):
        """Muestra/oculta el cursor"""
        if show:
            self.displaycontrol |= 0x02
        else:
            self.displaycontrol &= ~0x02
        self.write_cmd(0x08 | self.displaycontrol)
    
    def blink_cursor(self, blink=True):
        """Hace parpadear el cursor"""
        if blink:
            self.displaycontrol |= 0x01
        else:
            self.displaycontrol &= ~0x01
        self.write_cmd(0x08 | self.displaycontrol)
