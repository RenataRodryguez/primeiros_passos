# Frase: Curso em vídeo Python - tem 20 caracteres
# Fatiamento - Fatiar uma string, é conseguir pegar pedacos dela. comecando a contagem no zero
# Para pegar o indice dentro de uma string? Frase[9]n  ou frase[9:13] ou frase [1:12:2], frase[:5], frase[9::3], 
# Analise de string, como somar o cumprimento da frase? len(frase). 
# Contar quantas letras especificas tem na string? frase.count('o') ou frase.count('o',0,13)
# Encontrar pedaço especifico da string? frase.find('deo')
# Transformação: frase.replace('python', 'android')
# Upper, Lower frase.upper(), frase.lower(), frase.capitalize(letra maiuscula só no comeco da frase), frase.title(letra maiuscula em todas as palavras)
# Como remover espaco no comeco ou final da frase? frase.strip() / frase.rstrip() / frase.lstrip()
# Divisão considerando espaços? frase.split()
# Como juntar string? '-'.join(frase)
# Desafio: Crie um programa que leia o nome completo de uma pessoa e mostre: O nome dos todas as letras maiusculas, minusculas e qts letras tem ao todo sem considerar os espaços, e quantas letras tem o primeiro nome. 
nome = input('Digite seu nome')
print(nome.upper())
print(nome.lower())
print(len(nome))
dividido = nome.split()
print(dividido[0].count(0))

