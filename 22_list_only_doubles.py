Напишите программу, которая принимает на вход список чисел 
в одной строке и выводит на экран в одну строку значения, 
которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода 
может быть произвольным.

a = [int(i) for i in input().split()]
for i in set(a):
    if a.count(i) > 1:
        print(i, end=' ')
