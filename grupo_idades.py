#Desenvolva um programa que leia o nome idade e sexo de 4 pessoas e mostre:
#A média de idade do grupo
#O qual o nome do homem mais velho
#Quantas mulheres de menos de 20 anos

# Inicializando as variáveis
soma_idades = 0
idade_mais_velho = 0
nome_mais_velho = ''
mulheres_menos_20 = 0

# Loop para coletar dados de 4 pessoas
for c in range(4):
    nome = input(f'Digite o nome da {c + 1}ª pessoa: ').strip()
    idade = int(input(f'Digite a idade da {c + 1}ª pessoa: '))
    sexo = input(f'Digite o sexo da {c + 1}ª pessoa (M/F): ').strip().upper()

    # Soma todas as idades para calcular a média depois
    soma_idades += idade

    # Verifica se é homem e se é o mais velho até agora
    if sexo == 'M':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome

    # Verifica se é mulher e menor de 20 anos
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calcula a média
media_idades = soma_idades / 4

# Exibe os resultados
print(f'\nMédia de idade do grupo: {media_idades:.1f} anos')

if nome_mais_velho:
    print(f'O homem mais velho é {nome_mais_velho} com {idade_mais_velho} anos')
else:
    print('Nenhum homem foi cadastrado.')

print(f'Quantas mulheres têm menos de 20 anos: {mulheres_menos_20}')