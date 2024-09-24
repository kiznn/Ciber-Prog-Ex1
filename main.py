from lottery import Lottery

lottery = Lottery()

# Main program
while True:
   try:
       quantidade = int(input('Quantas? '))
       break
   except ValueError:
       print('Digite um número')

nums = []
starss = []
results = []
quantas = quantidade

while quantas > 0:
    # Generate lottery numbers and stars
    numeros, stars = lottery.create_arrays()

    if numeros not in nums and stars not in starss:
        lottery.sort_nums(numeros)
        lottery.sort_stars(stars)
        results = [numeros] + [stars]

        quantas -= 1

        print(f'Todos os resultado numero {quantidade-quantas} até agora: {results}')
    else:
        print(f'{numeros} ou {stars} são duplicados, gerando novamente...')

    input("Press Enter to continue...")
