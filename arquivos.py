# arquivo = open('curso-mvcad.csv', 'r')
# print(arquivo)

# arquivo = open('mvcad-exemplo.csv', 'r')
# print(arquivo.read)
#
# for line in arquivo
#     print(line)
# arquivo.writelines("oi tudo bem, Vivi?")
# print(arquivo)

#
# dicionario = {
#     'nome': "alini",
#     'idade': 30,
#     'cidade': 'blumenau',
#     'hobies': ['dorama', 'programar'],
#     'friorenta': False
import csv

# with open('mvcad-exemplo-csv.csv', 'w') as file:
#     escritor = csv.writer(file)
#     escritor.writerows(["Oi Vivi", "Tudo bem?"] )

with open('mvcad-exemplo-csv.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)