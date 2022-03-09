from data import Data
from generators import Generators as gen
import os,random
import time
import grafication

entrances = "lumu illuminates attacks and adversaries all Lorem ipsum dolor sit amet consectetur adipiscing elit Proin mollis ex tellus non ullamcorper vehicula ut Nunc tincidunt "
l_entrances = entrances.split(" ")
pid_process = os.getpid()


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
    result = {}
    data = Data(data).data_list
    for w,v in gen.generator_iter_mode_3(data):
        result[w] = v
    sorted_result = Data.sorted_values(result)
    sorted_result = { k:result[k] for k in sorted_result }

def cases(n):
    cases_list = ""
    for i in range(0,n):
        x = random.randint(0,23)
        cases_list += l_entrances[x]+" "
    
    cases_list = cases_list.rstrip()
    return cases_list

def run_generators(n_cases,iterations):
    result = {}
    for j in range(1,n_cases+1):
        times_mode_1 = 0
        times_mode_2 = 0
        times_mode_3 = 0
        for i in range(0,iterations):
            list_data = cases(j)
            start_time_case_1 = time.time()
            generator_mode_1(list_data)
            end_time_case_1 = time.time()
            start_time_case_2 = time.time()
            generator_mode_2(list_data)
            end_time_case_2 = time.time()
            start_time_case_3 = time.time()
            generator_mode_3(list_data)
            end_time_case_3 = time.time()
            times_mode_1 += (end_time_case_1 - start_time_case_1)
            times_mode_2 += (end_time_case_2 - start_time_case_2)
            times_mode_3 += (end_time_case_3 - start_time_case_3)
        result[str(j)] = {
            "mode_1":{
                "time": times_mode_1 / iterations
                },
            "mode_2":{
                "time":times_mode_2 / iterations
                },
            "mode_3":{
                "time":times_mode_3 / iterations
                },
        }
    return result

time_results = run_generators(10,10)
grafication.generate_grafics(time_results)





