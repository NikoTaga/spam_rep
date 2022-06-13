
while True:
    a = int(input('введите число..   0 - это выход'))
    if a == 0:
        print('выход')
        break
    print(f'{a} {"четное" if a % 2 == 0 else "нечетное"} число')