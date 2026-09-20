tipo_imovel = input("Digite o tipo de imóvel (casa, apartamento ou comercial):.").strip().lower()
consumoi = float(input("Digite o consumo mensal de água em m³:"))

match tipo_imovel:
    case "comercial":
        print("tarifa comercial aplicada - consulte o plano comercial.")

        case "apartamento" if consumo < 10:
        print ("consumo econômico - Parabéns pelo consumo!")

        case ("apartamento" | "casa") if (tipo_imovel == "apartamento" and consumo <=25) or (tipo_imovel =="casa" and consumo <=25):
        print("consumo moderado - dentro do normal.")

        case _:
        print("consumo excessivo - economize!")