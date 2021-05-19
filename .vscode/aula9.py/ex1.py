nums = []

for i in range(10):
    num = int(input(f'Digite o {i+1}ª número: '))
    nums.append(num)

for num in nums:
    print([num], end= ' ')