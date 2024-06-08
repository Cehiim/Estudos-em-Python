#Arthur De Pina Balduino Leitão - 32207840
#Cesar Hideki Imai - 32255659
#João Victor Dallapé Madeira - 32209592
#Luiz Henrique Bonilha Pasquinelli - 32224419
def multiplicar(m, m2):
  if (len(m[0]) != len(m2)):
    return "ERRO! ESSA MULTIPLICAÇÃO DE MATRIZES É IMPOSSÍVEL!"
  resp = [[0 for col in range(len(m2[0]))] for linha in range(len(m))]
  linha_resp = [0] * len(m2[0])
  count = 0
  for i in range(len(m)):
    for j in range(len(m2[0])):
      for k in range(len(m[0])):
        count += m[i][k] * m2[k][j]
      linha_resp[j] = count
      count = 0
    resp[i] = linha_resp[:]
  return resp


def preencher():
  l1 = int(input("Qual o número de Linhas do primeiro vetor:"))
  c1 = int(input("Qual o número de Colunas do primeiro vetor:"))
  m = [[0 for col in range(c1)] for linha in range(l1)]
  for i in range(l1):
    for j in range(c1):
      m[i][j] = int(
          input("Insira o elemento da linha " + str(i + 1) + " coluna " +
                str(j + 1) + ":"))
  return m


def leitura():
  arquivo1 = open("Matriz.txt", "r")
  l1 = len(arquivo1.readlines())
  arquivo1.seek(0)
  m = [0] * l1
  for i in range(l1):
    m[i] = arquivo1.readline().split(" ")
  arquivo1.close()
  for i in range(l1):
    for j in range(len(m[0])):
      m[i][j] = float(m[i][j].rstrip('\n'))
  return m

def mostra(matriz):
  nLinha = len(matriz)
  nColuna = len(matriz[0])
  for i in range(nLinha):
    for j in range(nColuna):
      print("{:.4f}".format(matriz[i][j]), end = " | ")
    print("")

print(
    "Qual a forma de acesso a matriz?\n1.Arquivo Matrix.txt \n2.Digitando a matriz."
)
menu = input()
if (menu == "1"):
  m = leitura()
elif (menu == "2"):
  m = preencher()
print("\nMatriz elevada a:")
exp = int(input())
print("\nMatriz original:")
mostra(m)
print("----------------------------------")
resp = multiplicar(m, m)
for i in range(exp - 2):
  resp = multiplicar(resp, m)  
print("A matriz elevada a " + str(exp) + " é:")
mostra(resp)
