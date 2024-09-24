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
quantas = quantidade

while quantas > 0:
    numeros = lottery.create_arrays()

    duplicado = False

    for num in nums:
        if num == numeros:
            duplicado = True
            break

    if not duplicado:
        nums.append(numeros)
        quantas -= 1
    else:
        print(f'{numeros} é duplicado')
        continue

    print(nums)
    input("Press Enter to continue...")