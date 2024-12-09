import random

# 1. Uzdevums - Spēļu kauliņa mešanas simulācija
def kaulinu_mesanas_simulacija(n):
    max_summa = 0  
    
    for gajiens in range(n):
        kaulins1 = random.randint(1, 6)
        kaulins2 = random.randint(1, 6)
        
        # Lielākā vērtība no abiem kauliņiem
        lielaka_vertiba = max(kaulins1, kaulins2)
        
        # Abu vērtību summa
        summa = kaulins1 + kaulins2
        
        # Izdod rezultātus
        print(f"Gājiens {gajiens + 1}: Kauliņš 1: {kaulins1}, Kauliņš 2: {kaulins2}, Lielākā vērtība: {lielaka_vertiba}, Summa: {summa}")
        
        # Pārbaudām, vai šī summa ir lielākā
        if summa > max_summa:
            max_summa = summa
    
    print(f"\nLielākā summu, kas tika uzmesta: {max_summa}")

# Piemērs: atkārtot kauliņu mešanu 10 reizes
n = 10
kaulinu_mesanas_simulacija(n)

# 2. Uzdevums - Lietotāja minēšanas spēle
def minesanas_speles():
    dators_skaitlis = random.randint(1, 100)
    minesanu_reizes = 0
    atrasts = False
    
    print("Izvēlētais intervāls ir no 1 līdz 100.")
    
    while not atrasts:
        minets_skaitlis = int(input("Ievadi savu minējumu: "))
        minesanu_reizes += 1
        
        if minets_skaitlis < dators_skaitlis:
            print("Lielāks!")
        elif minets_skaitlis > dators_skaitlis:
            print("Mazāks!")
        else:
            print("Uzminēts!")
            atrasts = True
    
    print(f"\nTev vajadzēja {minesanu_reizes} mēģinājumus, lai uzminētu skaitli.")

# Izsauc spēli
minesanas_speles()