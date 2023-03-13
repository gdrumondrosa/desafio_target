import json
import statistics

input_file = open ('dados.json')
json_array = json.load(input_file)

aux = 0
for e in json_array:
    if e["valor"] != 0:
        min = e["valor"]
        break

for e in json_array:
    if e["valor"] != 0:
        if e["valor"] < min:
            min = e["valor"]

print("Menor valor de faturamento ocorrido em um dia do mes: ", min)

max = 0

for e in json_array:
    if e["valor"] > max:
        max = e["valor"]

print("Maior valor de faturamento ocorrido em um dia do mes: ", max)

dias_not_null = []

for e in json_array:
    if e["valor"] != 0:
        dias_not_null.append(e["valor"])

mean = statistics.mean(dias_not_null)

days = 0

for e in dias_not_null:
    if e > mean:
        days = days + 1

print("Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal: ", days)