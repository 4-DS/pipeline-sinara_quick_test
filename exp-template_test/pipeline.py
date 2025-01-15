import sys, os
sys.path.append('../')

#Сделать из ноутбука функцию
# пишем файл exp.ipnb с кодом:
import sinara.experiment as exp

f1 = exp.Experiment.function("first.ipnb")
f2 = exp.Experiment.function("second.ipnb")
f3 = exp.Experiment.function("third.ipnb")


r1 = f1()
r2 = f2(r1.x, r1.y)
f3()
