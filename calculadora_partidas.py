def calcular_nivel(vitorias, derrotas):
  saldo_vitorias = vitorias - derrotas

  if saldo_vitorias <= 10:
    nivel = "Ferro"
  elif 11 <= saldo_vitorias <= 20:
    nivel = "Bronze"
  elif 21 <= saldo_vitorias <= 50:
    nivel = "Prata"
  elif 51 <= saldo_vitorias <= 80:
    nivel = "Ouro"
  elif 81 <= saldo_vitorias <= 90:
    nivel = "Diamante"
  elif 91 <= saldo_vitorias <= 100:
    nivel = "Lendário"
  else:
    nivel = "Imortal"

  mensagem = f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}"
  return mensagem

# Exemplo de uso:
vitorias = 75
derrotas = 20
resultado = calcular_nivel(vitorias, derrotas)
print(resultado)

vitorias = 150
derrotas = 50
resultado = calcular_nivel(vitorias, derrotas)
print(resultado)

vitorias = 5
derrotas = 8
resultado = calcular_nivel(vitorias, derrotas)
print(resultado)
