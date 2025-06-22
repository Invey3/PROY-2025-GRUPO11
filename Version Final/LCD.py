from time import localtime

# Nombres de los meses abreviados
MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", 
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

def obtener_fecha_hora():
    """Obtiene la fecha y hora actual formateada."""
    t = localtime()
    fecha = "{:3} {:02d}/ {:04d}".format(MESES[t[1]-1], t[2], t[0])
    hora = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])
    return fecha, hora

def inicializar_lcd(rs=16, e=17, d4=18, d5=19, d6=20, d7=21, lines=2, cols=16):
    """Inicializa el LCD y devuelve el objeto."""
    from lcd_1602 import LCD1602  # Importar aquí para evitar dependencia circular
    return LCD1602(rs, e, d4, d5, d6, d7, lines, cols)
