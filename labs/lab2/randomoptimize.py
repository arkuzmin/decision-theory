# -*- coding: utf-8 -*-
import random
import math

#Реализует метод случайного поиска
def randomoptimize(domain, costf):
    best = 999999999
    bestr = None
    for i in range(1000):
        # Выбираем случайное решение
        r = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
        # Вычисляем его стоимость
        cost = costf(r)
        # Выбираем лучшее 
        if cost < best:
            best = cost
            bestr = r
    return r