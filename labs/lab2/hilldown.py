# -*- coding: utf-8 -*-
import random
import math

# ��������� �������� ������ � ����
def hilldown(domain, costf):
    # �������� ��������� �������
    sol = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]

    # ������� ����
    while 1:
    
        # ������� ������ �������� �������
        neighbors=[]
        for j in range(len(domain)):

            # ������� �� ���� ��� � ������ �����������
            if sol[j] > domain[j][0]:
                neighbors.append(sol[0:j]+[sol[j]+1]+sol[j+1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j]+[sol[j]-1]+sol[j+1:])

        # ���� ��������� �� �������� �������
        current = costf(sol)
        best = current
        
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if cost < best:
                best = cost
                sol = neighbors[j]

        # ���� ��������� ���, �� �������� ���
        if best == current:
            break
            
    return sol