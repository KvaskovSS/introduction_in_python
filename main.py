import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))

def task1() :
    n = int(input("Введите количество элементов первого множества: "))
    m = int(input("Введите количество элементов второго множества: "))

    set1 = set()
    set2 = set()

    print("Введите элементы первого множества:")
    for i in range(n):
        set1.add(int(input()))

    print("Введите элементы второго множества:")
    for i in range(m):
        set2.add(int(input()))

    common_set = set1.intersection(set2)

    print("Общие элементы двух множеств:", sorted(common_set))

def task2() :
    n = int(input("Введите количество кустов: "))
    berries = list(map(int, input("Введите количество ягод на каждом кусте через пробел: ").split()))

    max_berries = 0

    for i in range(n):
        curr_berries = berries[i] + berries[(i+1)%n] + berries[(i+2)%n] # суммируем ягоды с текущего куста и двух соседних
        if curr_berries > max_berries:
            max_berries = curr_berries

    print("Максимальное количество ягод, которое может собрать собирающий модуль за один заход:", max_berries)
    
def main() :
    i = int(input("Выберите номер задание [1 ; 3]  : "))
    if i == 1 :
        task1()
    elif i == 2 :
        task2()

if __name__ == "__main__" :
    main()