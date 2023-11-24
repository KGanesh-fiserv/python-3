from pprint import pprint
import os
 
def build_car_list():
    #Get ipnut files from files directory
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir=dir.replace('src', 'files')
    os.chdir(dir)
   
    #Result list
    res = []
   
    #Open necessary files
    with open("input.txt", "r") as input, open("car-ids.txt", "r") as car_id:
        input.readline()
        while True:
            input_line = input.readline().strip()
            car_id_line = car_id.readline().strip()
            if not input_line or not car_id_line: break
 
            input_data = input_line.split(", ")
            car_id_data = car_id_line.split(", ")
            if float(input_data[1]).is_integer():
                res.append({'id': int(car_id_data[0]), 'miles': int(input_data[1]),'model': car_id_data[1]})
    return(res)
 
 
def ex5():
    car_list = build_car_list()
    pprint(car_list)
 
ex5()
