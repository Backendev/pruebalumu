from data import Data
from generators import Generators as gen
import big_o
import random
import os
entrance1 = """
lumu illuminates illuminates attacks lumu illuminates attacks lumu
"""#8-3
entrance2 = """
lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries
"""#16-6
entrance3 = """
lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries all Lorem ipsum dolor sit amet consectetur dolor dolor sit consectetur amet amet dolor consectetur consectetur
"""#32-12

entrance4 = """
lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries all Lorem ipsum dolor sit amet consectetur dolor dolor sit consectetur amet amet dolor consectetur  Lorem Lorem consectetur adipiscing elit Proin mollis ex tellus non ullamcorper vehicula ut Nunc tincidunt tincidunt tincidunt elit ex Proin tellus elit adipiscing non Proin elit ex tellus non Proin elit elit adipiscing mollis mollis mollis non
"""#68-24

pid_process = os.getpid()
print(pid_process)

cases = [entrance1,entrance2,entrance3,entrance4]
def generator_mode_1(data):
    result = {}
    data = Data(data).data_list
    for w,v in gen.generator_iter_mode_1(data):
        result[w] = v
    sorted_result = Data.sorted_values(result)
    sorted_result = { k:result[k] for k in sorted_result }

def generator_mode_2(data):
    result = {}
    data = Data(data).data_list
    for w,v in gen.generator_iter_mode_2(data):
        result[w] = v
    sorted_result = Data.sorted_values(result)
    sorted_result = { k:result[k] for k in sorted_result }

def generator_mode_3(data):
    print(data)
    result = {}
    data = Data(data).data_list
    for w,v in gen.generator_iter_mode_3(data):
        result[w] = v
    sorted_result = Data.sorted_values(result)
    sorted_result = { k:result[k] for k in sorted_result }

texts = lambda n: big_o.datagen.strings(100)

t = big_o.datagen.strings(100)

def generator_iter_cases():
    x = random.randint(0,3)
    return cases[x]


