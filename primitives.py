# -*- coding: utf-8 -*-

import math

# очень примитивы
def a_add(a, b): return a+b # сложение
def a_sub(a, b): return a-b # вычитание
def a_mul(a, b): return a*b # умножение
def a_div(a,b): return a/b # деление
def a_sqrt(a): return math.sqrt(abs(a)) # корень
def a_exponentiation(x, n): return x**n # возведение в степень
def a_first_elem(data_list): return data_list[0] # первый элемент
def a_last_elem(data_list): return data_list[-1] # последний элемент
def a_any_elem(data_list, pos): return data_list[pos] # произвольный элемент

# операции над векторами
def a_vec_sum(vec1, vec2): # сложение векторов
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem += vec2[pos]
        vec_result.append(elem)
    return vec_result
def a_vec_sub(vec1, vec2): # вычитание векторов
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem -= vec2[pos]
        vec_result.append(elem)
    return vec_result
def a_vec_mul(vec1, vec2): # умножить
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem *= vec2[pos]
        vec_result.append(elem)
    return vec_result
def a_vec_div(vec1, vec2): # делить
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem /= vec2[pos]
        vec_result.append(elem)
    return vec_result
def a_vec_sqrt(vec): # извлечь корень каждого значения
    for pos, elem in enumerate(vec):
        vec[pos] = math.sqrt(elem)
    return vec
def a_vec_exponentiation(vec, n): # возвести в степень
    for pos, elem in enumerate(vec):
        vec[pos] = elem**n
    return vec


# операции над всем списком фин.данных
def a_get_vec(data_list, pos):
    return data_list[pos]
def a_get_couple_vec(data_list, elem1pos, elem2pos):
    return [data_list[elem1pos], data_list[elem2pos]]
def a_cng_vec_pos(data_list, pos1, pos2):
    '''
    меняет местами векторы во входящем list'е данных
    '''
    data_list[pos1], data_list[pos2] \
    = data_list[pos2], data_list[pos1]
    return data_list
def a_sum_vec_to1(vec1, vec2): # суммируем векторы в один
    return vec_sum(vec1, vec2)
def a_div_vec_to1(vec1, vec2): # получаем отношение одного вектора к другому
    return vec_div(vec1, vec2)
def a_create_new_dimension(data_list, dimension):
    '''
    # крепим значения нового пространства напрямую, от начала наших данных
    >>> data_list = [[1,2,3],
                [3,4,5],
                [6,7,8]]
    >>> dimension = [1,2]
    >>> a_create_new_dimension(data_list, dimension)
    [[1,2,3,1], [3,4,5,2], [6,7,8]]
    >>>
    '''
    new_dimension_args_count = len(dimension)
    for pos, vector in enumerate(data_list):
        if pos >= new_dimension_args_count:
            break
        data_list[pos] = vector + list(dimension[pos])
def a_create_new_dimension_data_reversed(data_list, dimension):
    '''
    # крепим значения нового пространства напрямую, 
    # от начала наших данных, которые развернуты
    >>> data_list = [[1,2,3],
                [3,4,5],
                [6,7,8]]
    >>> dimension = [1,2]
    >>> a_create_new_dimension_data_reversed(data_list, dimension)
    [[6,7,8,1], [3,4,5,2], [1,2,3]]
    >>>
    '''
def a_create_new_dimension_all_reversed(data_list, dimension):
    '''
    # крепим значения нового развернутого пространства, 
    # от начала наших развернутых наоборот данных
    >>> data_list = [[1,2,3],
                [3,4,5],
                [6,7,8]]
    >>> dimension = [1,2]
    >>> a_create_new_dimension_data_reversed(data_list, dimension)
    [[6,7,8,2], [3,4,5,1], [1,2,3]]
    >>>
    '''