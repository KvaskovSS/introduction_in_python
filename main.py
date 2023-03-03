def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a+1, b-1)

def task1() :
    a = int(input("Введите число, которое нужно возвести в степень: "))
    b = int(input("Введите целую степень, в которую нужно возвести число: "))

    result = power(a, b)

    print(f"A = {a}; B = {b} -> {result}")

def task2() :
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    result = sum(a, b)

    print("Сумма чисел", a, "и", b, "=", result)
    
def main() :
    i = int(input("Выберите номер задание [1 ; 2]  : "))
    if i == 1 :
        task1()
    elif i == 2 :
        task2()

if __name__ == "__main__" :
    main()