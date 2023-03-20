def count_vowels(word):
    vowels = "aeiouy"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        row = []
        for j in range(1, num_columns+1):
            row.append(str(operation(i, j)))
        print("\t".join(row))

def multiply(x, y):
    return x * y

def sum(x, y):
    return x + y

def subtracting(x, y):
    return x - y

def division(x, y):
    if y == 0 :
        print("Нельзя делить на ноль ")
        return
    else :
        return x / y

def task1() :
    poem = input("Введите стихотворение: ")
    lines = poem.split()

    vowels_count = []
    for line in lines:
        words = line.split("-")
        count = sum(count_vowels(word) for word in words)
        vowels_count.append(count)

    if len(set(vowels_count)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

def task2() :
    task = int(input("Выберите операцию 1 - сложение \n 2 - вычитание \n 3 - умножение  \n 4 - деление \n"))
    x = int(input("Введите первое число : "))
    y = int(input("Введите второе число : "))
    if task == 1 :
        print_operation_table(sum, x, y)
    elif task == 2 :
        print_operation_table(subtracting, x, y)
    elif task == 3 :
        print_operation_table(multiply, x, y)
    elif task == 4 :
        print_operation_table(division, x, y)
    
def main() :
    i = int(input("Выберите номер   задание [1 ; 2]  : "))
    if i == 1 :
        task1()
    elif i == 2 :
        task2()

if __name__ == "__main__" :
    main()