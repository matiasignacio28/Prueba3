def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}

def iva_carrito(request):
	total=0
	if request.user.is_authenticated:
		if "carrito" in request.session.keys():
			for key, value in request.session["carrito"].items():
				total += round(value["acumulado"]*(0.19/1.19))
		
	return {"iva_carrito": total}

def subtotal_carrito(request):
	total=0
	if request.user.is_authenticated:
		if "carrito" in request.session.keys():
			for key, value in request.session["carrito"].items():
				total += round(value["acumulado"]/1.19)
		
	return {"subtotal_carrito": total}

def cantidad_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["cantidad"])
    return {"cantidad_carrito": total}
