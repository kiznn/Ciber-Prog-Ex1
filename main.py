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
quantas = quantidade

while quantas > 0:
    # Generate lottery numbers and stars
    numeros, stars = lottery.create_arrays()

    if numeros not in nums and stars not in starss:
        nums.append(numeros)
        starss.append(stars)

        results = [nums, starss]

        quantas -= 1  # Decrement the counter as we have added a valid entry

        print(f'Todos os resultados até agora: {results}')
    else:
        print(f'{numeros} ou {stars} são duplicados, gerando novamente...')

    input("Press Enter to continue...")
