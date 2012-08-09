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
    

class DecisionSet():
    '''
        Этот класс должен уметь работать с базами данных - добавляя в
        том числе данные в горизонтально-масштабируемые БД
        но это не самое главное..
        
        В нем должны содержаться перечисление всех функций(деревьев),
        которые получились, посредством применения
        библиотеки pyevolve.
    '''
    def add_tree(self):
        '''
        добавляет дерево БД существующих
        '''
        pass
    
    def get_tree(self):
        '''
        получает дерево из БД
        '''
        pass
    
    def eval_tree(self):
        '''
        получает результат работы дерева
        '''
        pass
        
    def write_result(self):
        '''
        пишет результат работы дерева в БД,
        соотнося его с существующим там деревом
        '''
        pass