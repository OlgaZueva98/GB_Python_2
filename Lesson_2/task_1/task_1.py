# Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и
# формирующий новый «отчетный» файл в формате CSV.


import re
import csv



def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []

    for i in range(1, 4):
        file_obj = open(f'info_{i}.txt')
        data = file_obj.read()




