"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    
    def check_strings(str1, str2):
        if type(str1) != str or type(str2) != str:
            return 0
        elif str1 == str2:
            return 1
        elif len(str1) > len(str2) and str2 == 'learn':
            return 3
        else:
            return 2

    print(check_strings('hello', 'hello'))
    print(check_strings('hello', 'world'))
    print(check_strings('hello', 'learn'))
    print(check_strings('hello', ''))
    print(check_strings('', ''))
    print(check_strings('', 'hello'))
    print(check_strings('hello', ''))

if __name__ == "__main__":
    main()
