import random

def gerar_palpite_mega_sena():
    palpite = []
    while len(palpite) < 6:
        numero = random.randint(1, 60)
        if numero not in palpite:
            palpite.append(numero)
    palpite.sort()
    return palpite
        
palpite = gerar_palpite_mega_sena()
print("Seu palpite da Mega-Sena é:", palpite)
