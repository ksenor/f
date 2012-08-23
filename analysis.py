# -*- coding: utf-8 -*-

class DataLoader():
    
    def load_data(self, file_name, pass_first_string=True):
        '''
        возвращает значения в виде матрицы: списка,
        состоящего из векторов вида:
        <DATE>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>
        '''
        
        with open(file_name) as loaded:
            all_lines = loaded.readlines()
            if pass_first_string:
                loaded_lines = all_lines[1:]
            else:
                loaded_lines = all_lines[:]
            loaded_data = []
            for line in loaded_lines:
                vector = line.split(',')
                vector[-1] = vector[-1].replace('\n', '')
                loaded_data.append(vector)
        return loaded_data
    

class DataCreater():
    '''
    # подаем на вход те данные, что лежат в DataLoader'е
    # получаем желательно как можно более разнообразные,
    т.е чтоб
    >>> fails_counter = { 'vectors': 0, 'elements': 0 }
    >>> for pos, vec in enumeration(data_list1):
    ...   for pos, elem in enumeration(vec):
    ...     if elem == ...
    # короче цель - все значения fails_counter - по-нулям..
    # если вектор полностью совпадает - добавляем в счетчик.
    # считаем и по относительным значения цель достигнута 
    # - если все по-нулям
    '''
        
    def __init__(self, data_inp):
        self.data_inp = data_inp
    
    