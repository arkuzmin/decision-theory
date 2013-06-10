#-*- coding: utf-8 -*-
# ����������� ������� PuLP
from pulp import *
 
# ������� ����� ������ ��������� ���������������� (LP) � ������������� ������� �������
prob = LpProblem("Knapsack problem", LpMaximize)
 
# ���������� �����������, �����
x1 = LpVariable("x1", 0, 10, 'Integer')
x2 = LpVariable("x2", 0, 10, 'Integer')
x3 = LpVariable("x3", 0, 10, 'Integer')
 
# ������� ������� ("�������� �������")
prob += 17*x1 + 30*x2 + 75*x3, "obj"
 
# ����������� ("��� �������")
prob += 1.5*x1 + 2.5*x2 + 6*x3 <= 20, "c1"
 
# ��������� ��������
prob.solve(GLPK(msg = 0))
 
# ������� ������ ������
print "Status:", LpStatus[prob.status]
 
# ������� ������������ ����������� �������� ����������
for v in prob.variables():
  print v.name, "=", v.varValue
 
# ������� ����������� �������� ������� �������
print ("objective = %s$" % value(prob.objective))