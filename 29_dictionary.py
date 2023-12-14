Когда Антон прочитал «Войну и мир», ему стало интересно,
сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, 
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и 
выводить для каждого уникального слова в этой строке число его 
повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным.

Sample Input 1: a aa abC aa ac abc bcd a
Sample Output 1: 
a 2
aa 2
ac 1
abc 2
bcd 1

Sample Input 2: a A a
Sample Output 2: a 3

words = input().lower().split(" ")
wordDict={}
for word in words:
    if wordDict.get(word) != None:
        wordDict[word] += 1
    else:
        wordDict.setdefault(word,1)
for key, value in wordDict.items():
    print(key, value)
