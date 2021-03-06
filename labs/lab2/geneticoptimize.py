# -*- coding: utf-8 -*-
import random
import math

# ���������� ������������� ���������
# popsize - ������ ���������
# step - �������� ��� �������
# mutprob - ����������� ����, ��� ����� ����� ����� ����������� �������, � �� �����������
# elite - ���� ������ � ���������, ����������� �������� ��������� � ����������� � ��������� ���������
# maxiter - ���������� ���������
#-------------------------------------------------------------
def geneticoptimize(domain, costf, popsize=50, step=1, mutprob=0.2, elite=0.2, maxiter=100):
    # �������� �������
    def mutate(vec):
        i = random.randint(0, len(domain) - 1)
        if random.random() < 0.5 and vec[i] > domain[i][0]:
            return vec[0:i] + [vec[i]-step] + vec[i+1:]
        elif vec[i] < domain[i][1]:
            x = (vec[0:i] + [vec[i] + step] + vec[i+1:])
            return vec[0:i] + [vec[i] + step] + vec[i+1:]
        elif vec[i] > domain[i][0]:
            return vec[0:i] + [vec[i]-step] + vec[i+1:]
        else:
            return vec
            
    # �������� �����������
    def crossover(r1, r2):
        i = random.randint(1, len(domain) - 2)
        #print (r1[0:i] + r2[i:])
        return r1[0:i] + r2[i:]
        
    # ������ ��������� ���������
    pop=[]
    for i in range(popsize):
        vec = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
        pop.append(vec)
    
    # ������� ����� ����������� �� ������ ���������?
    topelite = int(elite * popsize)
    
    # ������� ����
    for i in range(maxiter):
        
        # ��������� ��������� ��� ������� ������� � ���������
        scores = [(costf(v),v) for v in pop]
        scores.sort()
        ranked = [v for (s,v) in scores]
        
        # ������� �������� ������ �����������
        pop = ranked[0:topelite]
        
        # ��������� ������, ���������� �������� � ������������ ���������� ���������
        while len(pop) < popsize:
            if random.random() < mutprob:
                # �������
                c = random.randint(0, topelite)
                x = mutate(ranked[c])
                pop.append(mutate(ranked[c]))
            else:
                # �����������
                c1 = random.randint(0,topelite)
                c2 = random.randint(0,topelite)
                x = crossover(ranked[c1], ranked[c2]) 
                pop.append(crossover(ranked[c1], ranked[c2]))
                  
    return scores[0][1]