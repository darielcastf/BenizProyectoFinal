from db import conectar

productos = [
    # ---------------------
    # CUENTAS DE AHORRO
    # ---------------------
    ("Cuenta de Ahorro Digital", "Banco Popular", "Ahorro", 2.50, 0,
     "Cuenta digital sin monto mínimo y sin libreta, enfocada en jóvenes."),
    
    ("Cuenta Libre de Ahorro", "BHD León", "Ahorro", 2.80, 1000,
     "Cuenta tradicional de ahorro con disponibilidad inmediata."),
    
    ("Cuenta de Ahorro Navideño", "Banreservas", "Ahorro", 3.00, 500,
     "Cuenta programada para ahorro estructurado con aportes automáticos."),
    
    ("Cuenta APAP Móvil", "APAP", "Ahorro", 3.50, 0,
     "Cuenta digital sin monto mínimo y sin costos de mantenimiento."),

    # ---------------------
    # CERTIFICADOS FINANCIEROS (CDT)
    # ---------------------
    ("Certificado Financiero a 180 días", "BHD León", "Inversión", 8.00, 10000,
     "Certificado financiero de rendimiento fijo a seis meses."),
    
    ("Certificado Financiero a 360 días", "Banreservas", "Inversión", 8.75, 5000,
     "Certificado financiero anual con tasa competitiva."),
    
    ("Certificado Digital Flexible", "Banco Popular", "Inversión", 7.90, 10000,
     "Certificado digital con disponibilidad parcial."),
    
    ("Certificado de Ahorro Programado", "APAP", "Inversión", 7.50, 3000,
     "Certificado diseñado para metas financieras a mediano plazo."),

    # ---------------------
    # CUENTAS PARA JÓVENES
    # ---------------------
    ("Cuenta Joven", "BHD León", "Ahorro", 3.00, 500,
     "Cuenta para jóvenes entre 16 y 25 años, ideal para comenzar hábitos de ahorro."),
    
    ("Tarjeta Prepago Joven", "Banco Popular", "Prepago", 0.00, 500,
     "Tarjeta prepago recargable sin necesidad de historial crediticio."),

    # ---------------------
    # PEQUEÑOS INVERSIONISTAS
    # ---------------------
    ("Ahorro a Plazo Pequeño Inversionista", "Banreservas", "Inversión", 5.50, 1000,
     "Producto de bajo monto ideal para iniciarse en inversiones."),
    
    ("Cuenta Meta", "APAP", "Ahorro", 4.00, 0,
     "Ahorro enfocado en metas específicas con mejor rendimiento."),

    # ---------------------
    # PRÉSTAMOS
    # ---------------------
    ("Préstamo Personal", "Banreservas", "Préstamo", 18.00, 0,
     "Préstamo personal de aprobación rápida con plazos flexibles."),
    
    ("Préstamo Joven Profesional", "BHD León", "Préstamo", 15.00, 0,
     "Préstamo diseñado para jóvenes en el inicio de su vida laboral."),

    # ---------------------
    # TARJETAS Y PRODUCTOS ESPECIALES
    # ---------------------
    ("Tarjeta de Crédito Visa Joven", "Banco Popular", "Tarjeta", 0.00, 0,
     "Tarjeta para jóvenes con beneficios en entretenimiento y educación."),
    
    ("Cuenta de Ahorro Universitario", "Banreservas", "Ahorro", 3.20, 100,
     "Cuenta diseñada para estudiantes universitarios con beneficios académicos."),

    # ---------------------
    # QIK – PRODUCTOS DIGITALES (CORRECTAMENTE SEPARADOS)
    # ---------------------
    ("Qik Préstamo Digital", "Qik", "Préstamo", 20.00, 0,
     "Préstamo totalmente digital, aprobado en minutos desde la app."),
    
    ("Qik Cuenta Digital", "Qik", "Ahorro", 0.00, 0,
     "Cuenta digital sin papeleo, sin costos de mantenimiento y sin montos mínimos.")
]

conn = conectar()
cur = conn.cursor()

cur.executemany("""
INSERT INTO productos (nombre, entidad, tipo, tasa, minimo, descripcion)
VALUES (?, ?, ?, ?, ?, ?)
""", productos)

conn.commit()
conn.close()

print("Productos insertados correctamente.")
