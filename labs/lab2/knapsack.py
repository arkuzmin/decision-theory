#-*- coding: utf-8 -*-
# импортируем функции PuLP
from pulp import *
 
# Создаем новую задачу Линейного программирования (LP) с максимизацией целевой функции
prob = LpProblem("Knapsack problem", LpMaximize)
 
# Переменные оптимизации, целые
x1 = LpVariable("x1", 0, 10, 'Integer')
x2 = LpVariable("x2", 0, 10, 'Integer')
x3 = LpVariable("x3", 0, 10, 'Integer')
 
# Целевая функция ("ценность рюкзака")
prob += 17*x1 + 30*x2 + 75*x3, "obj"
 
# Ограничение ("вес рюкзака")
prob += 1.5*x1 + 2.5*x2 + 6*x3 <= 20, "c1"
 
# Запускаем решатель
prob.solve(GLPK(msg = 0))
 
# Выводим статус задачи
print "Status:", LpStatus[prob.status]
 
# Выводим получившиеся оптимальные значения переменных
for v in prob.variables():
  print v.name, "=", v.varValue
 
# Выводим оптимальное значение целевой функции
print ("objective = %s$" % value(prob.objective))