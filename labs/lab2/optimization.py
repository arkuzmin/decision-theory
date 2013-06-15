# -*- coding: utf-8 -*-

import time
import random
import math
import randomoptimize
import hilldown
import annealingoptimize
import geneticoptimize

# Инициализация семьи (имя, местро отправления)
#-------------------------------------------------------------
people = [(u'Семен','BOS'), 
          (u'Федор','DAL'),
          (u'Андрей','CAK'),
          (u'Артем','MIA'),
          (u'Никита','ORD'),
          (u'Иван','OMA')]

# Общее назначение
destination='LGA'

# Инициализация словаря полетов
#-------------------------------------------------------------
flights={}

for line in file('schedule.txt'):
  origin,dest,depart,arrive,price=line.strip( ).split(',')
  flights.setdefault((origin,dest),[])
  flights[(origin,dest)].append((depart,arrive,int(price)))

  
# Вспомогательные функции
#-------------------------------------------------------------

def printpeople():
  print '%10s%10s' % (u'Имя', u'Аэропорт')
  print '-------------------------------'
  for d in range(len(people)):
    name = people[d][0]
    origin = people[d][1]
    print '%10s%10s' % (name, origin);
  

# Смещение данного момента времени от начала суток в минутах
def getminutes(t):
  x=time.strptime(t,'%H:%M')
  return x[3]*60+x[4]
  
# Вывод на экран решения
def printschedule(r):
  print '%10s%2s%10s%2s%11s%2s%5s%2s%11s%2s%5s' % (u'Имя','|',u'Аэропорт','|',u'Время туда','|',u'Цена','|',u'Время обратно','|',u'Цена');
  print('------------------------------------------------------------------------------')
  for d in range(len(r)/2):
    intd = int(d)
    name=people[d][0];
    origin=people[d][1];
    out=flights[(origin,destination)][int(r[d])];
    ret=flights[(destination,origin)][int(r[d+1])];
    print '%10s%2s%10s%2s%5s-%5s%2s$%5s%2s%5s-%5s%2s$%5s' % (name,'|',origin,'|',out[0],out[1],'|',out[2],'|',ret[0],ret[1],'|',ret[2]);
  print('-------------------------------------------------------------------------------')

    
# Целевая функция.
# Учитываются:
#   - полная стоимость поездки
#   - общее время ожидания в аэропорту всеми членами семьи
#   - штраф, если арендованная машина возвращена позже назначенного часа
#-------------------------------------------------------------    
def schedulecost(sol):
  totalprice = 0
  latestarrival = 0
  earliestdep = 24*60
  
  # Получаем список прибывающих и убывающих рейсов
  for d in range(len(sol)/2):
    origin=people[d][1]
    outbound=flights[(origin,destination)][int(sol[d])]
    returnf=flights[(destination,origin)][int(sol[d+1])]
    
    # Полная стоимость = сумма цен на билеты туда и обратно 
    totalprice += outbound[2]
    totalprice += returnf[2]
    
    # Самый поздний прилет и самый ранний вылет
    if latestarrival < getminutes(outbound[1]):
      latestarrival = getminutes(outbound[1])
      
    if earliestdep > getminutes(returnf[0]): 
      earliestdep = getminutes(returnf[0])
    
  # В аэропорту все ждут прибытия последнего члена семьи.
  # Обратно все прибывают одновременно и ждут свои рейсы.
  totalwait = 0
  for d in range(len(sol)/2):
    origin = people[d][1]
    outbound = flights[(origin,destination)][int(sol[d])]
    returnf = flights[(destination,origin)][int(sol[d+1])]
    totalwait += latestarrival - getminutes(outbound[1])
    totalwait += getminutes(returnf[0]) - earliestdep
  
  # Требуется оплата дополнительного дня аренды
  if latestarrival > earliestdep: 
    totalprice += 50
  
  return totalprice + totalwait
  
# Оптимизация целевой функции
#-------------------------------------------------------------

# Метод случайного поиска  
def randomopt(domain,costf):
    return randomoptimize.randomoptimize(domain,costf)

# Метод спуска с горы
def hilldownopt(domain, costf):
    return hilldown.hilldown(domain, costf)
    
# Метод имитации отжига    
def annealingopt(domain, costf):
    return annealingoptimize.annealingoptimize(domain, costf)

# Генетический алгоритм
def geneticopt(domain, costf):
    return geneticoptimize.geneticoptimize(domain, costf)