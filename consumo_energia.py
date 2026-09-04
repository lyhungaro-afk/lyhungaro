#!/usr/bin/env python3

nome_aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

print("\n--- Resultado ---")
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo mensal estimado: {consumo_mensal:.2f} kWh")