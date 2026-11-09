sensores_raw = [
    {"sensor_id": " SENSOR-001", "temperatura": "24.5 °C", "ubicacion": " Oficina"},
    {"sensor_id": "SENSOR-002 ", "ubicacion": "Sala de Espera "},
    {"sensor_id": "SENSOR-003", "temperatura": "23.2 C", "ubicacion": " Fabrica Norte "},
    {"sensor_id": " SENSOR-004 ", "temperatura": "26.5", "ubicacion": " Laboratorio"},
    {"sensor_id": "SENSOR-005", "temperatura": "27.0°C"},
    {"sensor_id": " SENSOR-006", "ubicacion": "Zona de Descanso "},
    {"sensor_id": " SENSOR-007", "temperatura": "28.0°", "ubicacion": " Area de Produccion "},
    {"sensor_id": "SENSOR-008 ", "temperatura": "23.0°C"},
    {"sensor_id": "SENSOR-009","ubicacion": " Cuarto de Descanso "},
    {"sensor_id": "SENSOR-010", "temperatura": "25.5°C", "ubicacion": "Edificio Administrativo"},
    {"sensor_id": "SENSOR-011", "ubicacion": "Sala de Reuniones ", "temperatura": "22.0 C"},
    {"sensor_id": "SENSOR-012", "temperatura": "29.0°C", "ubicacion": " Area de Almacenamiento"},
    {"sensor_id": "SENSOR-013", "ubicacion": "Gimnasio ", "temperatura": "21.5 °C"},
    {"sensor_id": "SENSOR-014", "ubicacion": "Sala de Computadoras"},
    {"sensor_id": "SENSOR-015", "ubicacion": "Cafetería ", "temperatura": "30.0 °C"},
    {"sensor_id": "SENSOR-016", "temperatura": "24.0°C", "ubicacion": "Oficina de Recursos Humanos"},
    {"sensor_id": "SENSOR-017", "ubicacion": "Sala de Aprendizaje ", "temperatura": "26.5 C"},
    {"sensor_id": "SENSOR-018", "temperatura": "28.5°C", "ubicacion": " Area de Investigación"},
    {"sensor_id": "SENSOR-019", "ubicacion": "Biblioteca ", "temperatura": "25.0 C"},
    {"sensor_id": "SENSOR-020", "temperatura": "29.5°C", "ubicacion": "Area de Servicios"},
    {"sensor_id": "SENSOR-021", "ubicacion": "Entrada ", "temperatura": ""},
    {"sensor_id": "SENSOR-022", "temperatura": "25.5°C", "ubicacion": " "},
    {"sensor_id": "SENSOR-023"},
    {"sensor_id": "SENSOR-024", "ubicacion": "Sala de Espera", "temperatura": "24.5 °C"},
    {"sensor_id": "SENSOR-025", "temperatura": "28.0°", "ubicacion": " Area de Produccion"},
    {"sensor_id": "SENSOR-026", "ubicacion": "Zona de Descanso", "temperatura": "26.0 C"}
]

sensores_limpios = []
umbral_temperatura = 27


def limpiar_registro_sensor(registro_raw:dict[str, str]): # toma un diccionario y devuelve un diccionario con datos limpios
    sensor_id_limpio = registro_raw.get("sensor_id", "SENSOR-DESCONOCIDO").strip()
    temperatura_limpia = registro_raw.get("temperatura", "").replace("°", "").replace("C", "").strip()
    if temperatura_limpia != "":
        temperatura_limpia = float(temperatura_limpia)
    else:
        temperatura_limpia = "TEMPERATURA DESCONOCIDA"
    ubicacion_limpia = registro_raw.get("ubicacion", "UBICACION DESCONOCIDA").strip()

    return {
        "sensor_id": sensor_id_limpio,
        "temperatura": temperatura_limpia,
        "ubicacion": ubicacion_limpia
    }


def generar_resumen_sensores():

    lista_sensores_alerta = []
    lista_temperaturas = []

    for sensor in sensores_limpios:
        if sensor["temperatura"] != "TEMPERATURA DESCONOCIDA":
            lista_temperaturas.append(sensor.get("temperatura"))
            if sensor["temperatura"] >= umbral_temperatura:
                        lista_sensores_alerta.append(sensor.get("sensor_id"))

    if lista_sensores_alerta == []:
        lista_sensores_alerta = "No hay Sensores en Alerta"

    if lista_temperaturas == []:
        lista_temperaturas = "No hay Temperaturas"
    else:
        prom_temperaturas = sum(lista_temperaturas) / len(lista_temperaturas)

    return (lista_sensores_alerta, prom_temperaturas)



if __name__ == "__main__":
    
    for registro in sensores_raw:
        registro_limpio = limpiar_registro_sensor(registro)
        sensores_limpios.append(registro_limpio)

    lista_sensores_alerta, prom_temperaturas = generar_resumen_sensores()


    print("SISTEMA DE MONITOREO DE SENSORES DE TEMPERATURA")
    print("=================================")
    print("Listado de Sensores Recibidos")
    for sensores in sensores_raw:
        print(sensores)
    print("=================================")
    print("Listado de Sensores Limpios")
    for sensores in sensores_limpios:
        print(sensores)
    print("=================================")
    print("Temperatura promedio global de la planta: ", prom_temperaturas, "°C")
    print("=================================")
    print("Umbral establecido de alerta: ", umbral_temperatura, "°C")
    print("=================================")
    print("Sensores alertados por exceso de temperatura: ", lista_sensores_alerta)
    print("=================================")
    print("FINAL DEL PROGRAMA")
