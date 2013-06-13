# -*- coding: utf-8 -*-
import random
import math

#��������� ����� ���������� ������
def randomoptimize(domain, costf):
    best = 999999999
    bestr = None
    for i in range(1000):
        # �������� ��������� �������
        r = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
        # ��������� ��� ���������
        cost = costf(r)
        # �������� ������ 
        if cost < best:
            best = cost
            bestr = r
    return r