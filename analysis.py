# -*- coding: utf-8 -*-

class DataLoader():
    
    def __init__(self, filename, pass_first_string=True):

        super(DataLoader, self).__init__()
        self.filename = filename
        self.pass_first_string = pass_first_string
        self.loaded_data = self.load_data()
    
    def load_data(self, file_name, pass_first_string):
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
                vector[-1] = vector[-1].replace('\n')
                loaded_data.append(vector)
        return loaded_data
