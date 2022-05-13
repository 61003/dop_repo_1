N = int(input("Введите N "))
for n in range(1, N + 1):
    for digit in range(1, 11):
        print(f'{n} X {digit} = {n * digit}')
    if n < N:
        print('-----')
