# -*- coding: utf-8 -*-

class DataLoader():
    
    def load_data(self, file_name, pass_first_string=True):
        '''
        возвращает значения в виде матрицы значений: списка,
        состоящего из списков вида:
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
    

class OperationSet():
    '''
        Этот класс должен уметь работать с базами данных - добавляя в
        том числе данные в горизонтально-масштабируемые БД
        но это не самое главное..
        
        В нем должны содержаться перечисление всех функций(их примитивов),
        которые подлежат дальнейшей компоновке, посредством
        библиотеки pyevolve.
    '''
    
    def get_operation(self):
        pass
        
    def set_operation(self):
        pass