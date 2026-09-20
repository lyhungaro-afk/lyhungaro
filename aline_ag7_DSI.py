tipo_imovel = input("Digite o tipo de imóvel (casa, apartamento ou comercial): ").strip().lower()
consumo = float(input("Digite o consumo mensal de água em m³: "))

match tipo_imovel:
    case "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
        
    case "apartamento" if consumo < 10:
        print("Consumo econômico – excelente controle de água!")
        
    case ("apartamento" | "casa") if (tipo_imovel == "apartamento" and consumo <= 25) or (tipo_imovel == "casa" and consumo <= 25):
        print("Consumo moderado – dentro do normal.")
        
    case _:
        print("Consumo excessivo – economize!.")