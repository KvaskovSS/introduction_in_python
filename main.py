def task1() :
    n = int(input("Введите длину массива N :"))
    arr = [i for i in range(n)]
    x = int(input("Введите искомое число :"))
    count = 0
    for i in arr :
        if arr[i] == x :
            count += 1
    print(f"{count}")




def task2() :
    n = int(input("Введите длину массива N :"))
    arr = [i for i in range(n)]
    x = int(input("Введите искомое число :"))
    res = arr[0]
    for i in arr:
        if abs(i - x) < abs(res - x):
            res = i
    print(res)

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
    
    n = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
    word = input('Введите слово: ').upper()
    if n == 1 :
	    print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
    elif n == 0 :
    	print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
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