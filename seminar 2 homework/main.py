def task1() :
    n = int(input("Введите число монеток на столе : "))
    count_heads = 0
    count_tails = 0
    for i in range(n):
        x = int(input())
        if x == 0 :
            count_tails += 1
        else : 
            count_heads += 1
    print(count_heads if count_heads < count_tails else count_tails)



def task2() :
    X, Y = int(input("Введите число X : ")), int(input("Введите число Y : "))
    for i in range(X) :
        for j in range(Y) :
            if X == i + j and Y == i * j :
                print(f"({X} ; {Y})")

def task3() :
    print("Все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")
    num = int(input("Введите число N : "))
    for i in range(num + 1) :
        print(f"{2 ** i} ")


def main() :
    i = int(input("Выберите номер задание [1 ; 4]  : "))
    if i == 1 :
        task1()
    elif i == 2 :
        task2()
    elif i == 3 :
        task3()
    #elif i == 4 :
        #task4()

if __name__ == "__main__" :
    main()