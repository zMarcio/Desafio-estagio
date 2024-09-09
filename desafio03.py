import json
"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
"""

"""Vetor criado por IA para simular faturamento diário"""


# teste = open('faturamento.json', "r")
# faturamento = json.load(teste).values()
# teste.close()
# print(faturamento)



def calcFaturamento(faturamento: str):  
    with open(faturamento, "r") as teste:
        dados = json.load(teste)
    faturamento_diario = []
    for chave, valor in dados.items():
        if isinstance(valor, list):
            faturamento_diario.extend(valor)
            
    menor = min(faturamento_diario)
    maior = max(faturamento_diario)
    media = round(sum(faturamento_diario) / len(faturamento_diario), 2)
    dias_acima_media = sum(valor > media for valor in faturamento_diario)

    
    return f"menor: {menor}, maior: {maior}, media: {media} e dias acima da média: {dias_acima_media}"
    
print(calcFaturamento("faturamento.json"))
