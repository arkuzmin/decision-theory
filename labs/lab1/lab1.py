# -*- coding: utf-8 -*-

import docclass
import feedfilter

print '=========================================\n'
print u'Классификатор Фишера \n'
print '========================================='
c1=docclass.fisherclassifier(docclass.getwords)
c1.setdb('feeds.db')
print u'Этап 1: Обучение классификатора'
feedfilter.read('feeds_train.xml', c1)
print '\n========================================='
print u'Этап 2: Проверка работы классификатора - используется база feeds.db'
feedfilter.test('feeds_test.xml', c1)

raw_input()