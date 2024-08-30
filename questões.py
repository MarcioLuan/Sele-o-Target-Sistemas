"""
1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(f"A soma é de  {soma}")

"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

numero = int (input ("Informe um número para verificar se ele faz parte da sequência de Fiboacci: "))
fibonacci = []
valor_anterior1 = 0
valor_anterior2 = 1

fibonacci.append(valor_anterior1)
fibonacci.append(valor_anterior2)

while valor_anterior2 <= numero:
    soma= valor_anterior1 + valor_anterior2
    valor_anterior1= valor_anterior2
    valor_anterior2= soma
    fibonacci.append(soma)

if numero in fibonacci:
    print(f"O número {numero} faz parte da sequência de Fibonacci")
else:
    print(f"O número {numero} não faz parte da sequência de Fibonacci")


"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar,
 que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json


def calcular_faturamento(dados):
    #Armazenando os faturamentos maiores que zero
    faturamentos = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

    #Obtendo o menor e o maior faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    # Calculando a média de faturamento mensal
    media_faturamento_mensal = sum(faturamentos) / len(faturamentos)

    # Contando o número de dias com faturamento acima da média de faturamento mensal
    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Carregando os dados a partir de um arquivo JSON chamado "faturamento_mensal"
with open('faturamento_mensal.json', 'r') as file:
    dados_faturamento = json.load(file)

# Chamando função calcular_faturamento para obter o menor e maior faturamentos e o número de dias com faturamento acima da média.
menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(dados_faturamento)

# Exibindo os resultados
print(f"O menor faturamento foi de R$ {menor_faturamento:.2f}")
print(f"O maior faturamento foi de R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")


