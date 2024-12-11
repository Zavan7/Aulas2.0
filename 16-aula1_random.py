import random

r = random.randrange(10, 200, 2)
r2 = random.randint(1, 10)
r3 = random.uniform(10, 20)

nomes = ['Vitor', 'Isabelle', 'Zavan']
random.shuffle(nomes)
print(nomes)
novos_nomes = random.sample(nomes, k = 3)
print(novos_nomes)

novos_nomes2 = random.choices(nomes, k = 2)
print(novos_nomes2)
