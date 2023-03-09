def task1() :
    a1 = int(input('Введите первый элемент: '))
    d = int(input('Введите разность: '))
    n = int(input('Введите количество элементов: '))

    progression = []
    for i in range(n):
        progression.append(a1 + i*d)

    print(progression)

def task2() :
    a1 = int(input('Введите первый элемент: '))
    d = int(input('Введите разность: '))
    n = int(input('Введите количество элементов: '))
    min_value = int(input('Введите минимальное значение: '))
    max_value = int(input('Введите максимальное значение: '))

    progression = []
    for i in range(n):
        progression.append(a1 + i*d)

    indices = []
    for i in range(n):
        if min_value <= progression[i] <= max_value:
            indices.append(i)

    print('Массив:', progression)
    print('Индексы элементов, значения которых принадлежат заданному диапазону:', indices)
    
def main() :
    i = int(input("Выберите номер задание [1 ; 2]  : "))
    if i == 1 :
        task1()
    elif i == 2 :
        task2()

if __name__ == "__main__" :
    main()