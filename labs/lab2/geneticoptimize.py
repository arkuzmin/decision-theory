# -*- coding: utf-8 -*-
import random
import math

# Реализация генетического алгоритма
def geneticoptimize(domain, costf, popsize=50, step=1, mutprob=0.2, elite=0.2, maxiter=100):
    # Операция мутации
    def mutate(vec):
        i = random.randint(0, len(domain) - 1)
        if random.random( ) < 0.5 and vec[i] > domain[i][0]:
            return vec[0:i] + [vec[i]-step] + vec[i+1:]
        elif vec[i] < domain[i][1]:
            return vec[0:i] + [vec[i] + step] + vec[i+1:]
            
    # Операция скрещивания
    def crossover(r1, r2):
        i = random.randint(1, len(domain) - 2)
        return r1[0:i] + r2[i:]
        
    # Строим начальную популяцию
    pop=[]
    for i in range(popsize):
        vec = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
        pop.append(vec)
        
    # Сколько брать победителей из каждой популяции?
    topelite = int(elite * popsize)
    
    # Главный цикл
    for i in range(maxiter):
        scores=[(costf(v),v) for v in pop]
        scores.sort()
        ranked=[v for (s,v) in scores]
        
        # Сначала включаем только победителей
        pop = ranked[0:topelite]

        # Добавляем особей, полученных мутацией и скрещиванием победивших родителей
        while len(pop) < popsize:
            if random.random( ) < mutprob:
                # Мутация
                c = random.randint(0,topelite)
                pop.append(mutate(ranked[c]))
            else:
                # Скрещивание
                c1 = random.randint(0,topelite)
                c2 = random.randint(0,topelite)
                pop.append(crossover(ranked[c1], ranked[c2]))
                
        # Печатаем полученные к текущему моменту наилучшие результаты
        print scores[0][0]
    return scores[0][1]