# -*- coding: utf-8 -*-
import random
import math

#Реализует метод "Имитации отжига"
def annealingoptimize(domain,costf,T=10000.0,cool=0.95,step=1):
    # Инициализировать переменные случайным образом
    vec = [float(random.randint(domain[i][0],domain[i][1])) for i in range(len(domain))]

    while T > 0.1:
        # Выбрать один из индексов
        i = random.randint(0, len(domain) - 1)
        
        # Выбрать направление изменения
        dir = random.randint(-step, step)

        # Создать новый список, в котором одно значение изменено
        vecb = vec[:]
        vecb[i] += dir
        if vecb[i] < domain[i][0]: vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]: vecb[i] = domain[i][1]

        # Вычислить текущую и новую стоимость
        ea = costf(vec)
        eb = costf(vecb)
        p = pow(math.e,(-eb-ea) / T)
        
        # Если новое решение не лучше - пробуем случайное
        if (eb < ea or random.random( ) < p):
            vec = vecb
        
        # Уменьшить температуру
        T = T * cool
        
    return vec