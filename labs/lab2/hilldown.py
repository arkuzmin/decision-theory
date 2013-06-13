# -*- coding: utf-8 -*-
import random
import math

# Реализует алгоритм спуска с горы
def hilldown(domain, costf):
    # Выбираем случайное решение
    sol = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]

    # Главный цикл
    while 1:
    
        # Создать список соседних решений
        neighbors=[]
        for j in range(len(domain)):

            # Отходим на один шаг в каждом направлении
            if sol[j] > domain[j][0]:
                neighbors.append(sol[0:j]+[sol[j]+1]+sol[j+1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j]+[sol[j]-1]+sol[j+1:])

        # Ищем наилучшее из соседних решений
        current = costf(sol)
        best = current
        
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if cost < best:
                best = cost
                sol = neighbors[j]

        # Если улучшения нет, мы достигли дна
        if best == current:
            break
            
    return sol