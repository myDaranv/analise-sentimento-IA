# Análise de Sentimento Simples (Regra Manual)
# Projeto introdutório para portfólio

texto = "eu gostei muito desse produto"

palavras_positivas = ["bom", "ótimo", "gostei", "excelente", "feliz"]
palavras_negativas = ["ruim", "péssimo", "odiei", "triste", "horrível"]

positivo = 0
negativo = 0

for palavra in palavras_positivas:
    if palavra in texto:
        positivo += 1

for palavra in palavras_negativas:
    if palavra in texto:
        negativo += 1

if positivo > negativo:
    sentimento = "Positivo"
elif negativo > positivo:
    sentimento = "Negativo"
else:
    sentimento = "Neutro"

print("Texto analisado:", texto)
print("Sentimento detectado:", sentimento)
