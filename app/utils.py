from datetime import datetime, timedelta

def get_status(fecha_caducidad):
    hoy = datetime.now().date()
    if fecha_caducidad < hoy:
        return "Vencido"
    elif fecha_caducidad <= hoy + timedelta(days=3):
        return "Por vencer"
    else:
        return "Vigente"