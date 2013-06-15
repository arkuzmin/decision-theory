# -*- coding: utf-8 -*-
import optimization


def printschedule(name, s):
  print(name)
  print('----------------------------------')
  optimization.printschedule(s)

def printresults(rand, hill, anneal, gen):
  print '%15s%2s%10s' % (u'Алгоритм', '|', u'Стоимость');
  print('----------------------------------')
  print '%15s%2s%10s' % (u'Случайный поиск', '|', rand);
  print '%15s%2s%10s' % (u'Спуск с горы', '|', hill);
  print '%15s%2s%10s' % (u'Имитация отжига', '|', anneal);
  print '%15s%2s%10s' % (u'Генетический', '|', gen);
  print('----------------------------------')


print(u'1. Исходные данные:')
print('----------------------------------')
optimization.printpeople()
print('')
print(u'Аэропорт встречи: ')
print(optimization.destination)
print('')
print('')

print(u'2. Оптимизация:')
print('----------------------------------')
domain = [(0,8)]*(len(optimization.people)*2)

print(u'2.1 Алгоритм случайного поиска...')
srand = optimization.randomopt(domain, optimization.schedulecost);
rand = optimization.schedulecost(srand)
print('')

print(u'2.2 Алгоритм спуска с горы...')
shill = optimization.hilldownopt(domain, optimization.schedulecost);
hill = optimization.schedulecost(shill)
print('')

print(u'2.3 Алгоритм имитации отжига...')
sanneal = optimization.annealingopt(domain, optimization.schedulecost);
anneal = optimization.schedulecost(sanneal)
print('')

print(u'2.4 Генетический алгоритм...')
sgen = optimization.geneticopt(domain, optimization.schedulecost);
gen = optimization.schedulecost(sgen)
print('')

print(u'3. Результаты:')
print('----------------------------------')
printresults(rand, hill, anneal, gen)

print('')
printschedule(u'Алгоритм случайного поиска', srand)
print('')
printschedule(u'Алгоритм спуска с горы', shill)
print('')
printschedule(u'Алгоритм имитации отжига', sanneal)
print('')
printschedule(u'Генетический алгоритм', sgen)

raw_input()

