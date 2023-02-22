def task1() :
    num = int(input('Введите 3-х значное число : '))
    if len(str(num)) != 3 :
        print('Число должно быть 3-х значным')
        return
    sum = 0
    for i in range(0, 3, 1) :
        temp = num % 10
        num //= 10
        sum += temp
    print(sum)


def task2() :
    ## x - pet x - serg 4x - k найти чему равен х  6x = s x = s/6
    S = int(input('Введите число журавликов : '))
    if S % 6 != 0 :
        print("Число журавликов должно быть кратно 6 (иначе получаются знаменитые полтора землекопа")
        return
    x = S // 6
    Petya = x
    Seryozha = x
    Katya = 4 * x

    print(f"Серёжа сделал - {Seryozha} \n Петя сделал -  {Petya} \n Катя сделала -  {Katya}" )


# 123 | 456 
def task3() :
    ticket = int(input("Введите номер билетика :"))
    if len(str(ticket)) != 6 :
        print("Номер билетика должен быть шестизначным числом") 
        return
    sumRight = 0
    sumLeft = 0
    i = 0
    while ticket != 0 :
        if i < 3 :
            sumRight += ticket % 10
            ticket //= 10
        else :
            sumLeft += ticket % 10
            ticket //= 10
        i += 1
    if sumRight == sumLeft :
        print("YES")
    else :
        print("NO")

def task4() :
    print("У нас имеется шоколадка m на n и мы будем определять модно ли от неё отрезать k долек по прямой")
    n,m,k = int(input("Введите n : ")),int(input("Введите m : ")),int(input("Введите k : "))
    if n * m > k:
        if k % n == 0 or k % m == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

def main() :
    i = int(input("Выберите номер задание [1 ; 4]  : "))
    if i == 1 :
        task1()
    elif i == 2 :
        task2()
    elif i == 3 :
        task3()
    elif i == 4 :
        task4()

if __name__ == "__main__" :
    main()