#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
#вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

#n = int(input('введите количество монет: '))
#k = 0
#for i in range(n):
#    v = int(input())
#    if v == 1:
#        k += 1
#print(f"минимальное количество монет, которые нужно перевернуть{k if k<n/2 else n-k}")

import random
from random import randint
amount_coin = int(input('введите количество монет: '))
m = 0
k = 0
coins = [0, 1]
for i in range(amount_coin):
     random.shuffle(coins)
     print(f'все монеты{coins}')
     if int(coins[0]) == 0:
         k += 1
     if int(coins[0]) == 1:
         m += 1
print(f'всего монет {m, k}')
if m > k:
    ans = k
else:
    ans = m
print(f"минимальное количество монет, которые нужно перевернуть{ans}")

#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#Помогите Кате отгадать задуманные Петей числа.

sum = int(input('Введите сумму чисел: '))
product = int(input('Введите произведение чисел: '))
X = (sum-int((sum**2-4*product)**0.5))//2
Y = sum - X
print(f'числа задуманные Петей{X, Y}')


#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
N = int(input('Введите целое число больше 1: '))
k=1
while k<=N:
   print(k,end=' ')
   k=k*2