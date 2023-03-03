import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))

def task1() :
    n = int(input("Введите длину массива N :"))

    list = []
    list.append(1)
    print("Заполните массив : ")
    for i in range(n - 1) :
        list.append(int(input()))
    print(list)
    x = int(input("Введите искомое число :"))
    count = 0
    for i in range(n):
        if list[i] == x :
            count += 1
    print(count)

def task2() :
    n = int(input("Введите длину массива N :"))
    list = []
    list.append(1)
    print("Заполните массив : ")
    for i in range(n - 1) :
        list.append(int(input()))
    print(list)
    x = int(input("Введите искомое число :"))
    
    min = abs(x - list[0])
    index = 0
    for i in range(1, n):
        count = abs(x - list[i])
        if count < min:
            min = count
            index = i
    print(list[index])

def task3() :
    eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
    rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
    text = input("Введите слово : ").upper()
    if isCyrillic(text) :
        print(sum([k for i in text for k, v in rus.items() if i in v]))
    else :
	    print(sum([k for i in text for k, v in eng.items() if i in v]))
    
def main() :
    i = int(input("Выберите номер задание [1 ; 3]  : "))
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