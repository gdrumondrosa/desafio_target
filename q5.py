string = input("Insira uma string: ")
string_len = (len(string))

reversed_string = []

for e in range(string_len):
    reversed_string.append(string[string_len-e-1])

print("String invertida: ", ''.join(reversed_string))