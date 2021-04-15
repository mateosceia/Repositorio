def cuanto_tardo_en_pagar_deposito():
    costo_total=input("¿Cuánto vale la casa que te gustaría comprar? ")
    sueldo_anual=input("¿Cuál es tu sueldo anual? ")
    porcentaje_ahorrado=input("¿Qué porcentaje de tu sueldo ahorras por mes? ")
    sueldo_mensual=float(sueldo_anual)/12
    porcentaje_deposito=0.25
    ganancia_anual=0.04
    cantidad_ahorrada=0
    ahorro_mensual=float(porcentaje_ahorrado)*sueldo_mensual
    ganancia_mensual=ahorro_mensual*(ganancia/12)
    total_mensual=ahorro_mensual+ganancia_mensual
    deposito=float(costo_total)*porcentaje_deposito
    meses_para_deposito=round((deposito/total_mensual)+0.5)
    print("Te tomará "+str(meses_para_deposito)+" meses ahorrar el dinero necesario para pagar el depósito.")