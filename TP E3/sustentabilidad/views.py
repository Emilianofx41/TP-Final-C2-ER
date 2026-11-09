from django.shortcuts import render

from .services import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):

    registro_historico = [
    {"planta": "Planta Norte", "consumo_Kwh": 1200.0},
    {"planta": "Planta Sur", "consumo_Kwh": 3400.0},
    {"planta": "Planta Este", "consumo_Kwh": 2000.0},
    {"planta": "Planta Oeste", "consumo_Kwh": 1500.0},
    {"planta": "Planta Norte", "consumo_Kwh": 200.0},
    ]

    metricas = obtener_metricas_consumo(registro_historico)

    contexto = {
        "total_emisiones": metricas["total_global_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "detalle_emisiones": metricas["emisiones_por_planta"]
    }

    return render(request, 'sustentabilidad/panel.html', contexto)
