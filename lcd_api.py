from machine import Pin
from time import sleep_ms

class LCD:
    def __init__(self, rs, en, d4, d5, d6, d7):
        self.rs = Pin(rs, Pin.OUT)
        self.en = Pin(en, Pin.OUT)
        self.data_pins = [Pin(d4, Pin.OUT), Pin(d5, Pin.OUT), Pin(d6, Pin.OUT), Pin(d7, Pin.OUT)]
        self.row_offsets = [0x00, 0x40, 0x14, 0x54]  # para 4 líneas (2 suficientes)
        self._init_lcd()

    def _pulse_enable(self):
        self.en.off()
        sleep_ms(1)
        self.en.on()
        sleep_ms(1)
        self.en.off()
        sleep_ms(1)

    def _send_nibble(self, nibble):
        for i in range(4):
            self.data_pins[i].value((nibble >> i) & 1)
        self._pulse_enable()

    def _send_byte(self, byte, is_data):
        self.rs.value(is_data)
        self._send_nibble(byte >> 4)
        self._send_nibble(byte & 0x0F)
        sleep_ms(2)

    def command(self, cmd):
        self._send_byte(cmd, is_data=False)

    def write_char(self, char):
        self._send_byte(ord(char), is_data=True)

    def write(self, message):
        for char in message:
            self.write_char(char)

    def clear(self):
        self.command(0x01)
        sleep_ms(2)

    def home(self):
        self.command(0x02)
        sleep_ms(2)

    def putstr(self, string):  # ← necesario
        self.write(string)

    def move_to(self, col, row):  # ← necesario
        if row > 3:
            row = 3
        addr = col + self.row_offsets[row]
        self.command(0x80 | addr)

    def _init_lcd(self):
        sleep_ms(20)
        self._send_nibble(0x03)
        sleep_ms(5)
        self._send_nibble(0x03)
        sleep_ms(5)
        self._send_nibble(0x03)
        sleep_ms(5)
        self._send_nibble(0x02)
        self.command(0x28)  # 4-bit, 2 lines, 5x8 font
        self.command(0x0C)  # Display on, cursor off
        self.command(0x06)  # Entry mode
        self.clear()
        