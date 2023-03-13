estados = []
estados.append({"nome": "sp", "faturamento": 67836.43})
estados.append({"nome": "rj", "faturamento": 36678.66})
estados.append({"nome": "mg", "faturamento": 29229.88})
estados.append({"nome": "es", "faturamento": 27165.48})
estados.append({"nome": "outros", "faturamento": 19849.53})

total = 0

for e in estados:
    total = total + e["faturamento"]

print("Percentual de representacao que cada estado teve dentro do valor total mensal da distribuidora:")
for e in estados:
    print(e["nome"], " = ", round((e["faturamento"]/total)*100, 2), "%")