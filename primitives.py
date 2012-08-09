# -*- coding: utf-8 -*-

import math

# очень примитивы
def add(a, b): return a+b # сложение
def sub(a, b): return a-b # вычитание
def mul(a, b): return a*b # умножение
def div(a,b): return a/b # деление
def sqrt(a): return math.sqrt(abs(a)) # корень
def exponentiation(x, n): return x**n # возведение в степень
def first_elem(data_list): return data_list[0] # первый элемент
def last_elem(data_list): return data_list[-1] # последний элемент
def any_elem(data_list, pos): return data_list[pos] # произвольный элемент

# операции над векторами
def vec_sum(vec1, vec2): # сложение векторов
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem += vec2[pos]
        vec_result.append(elem)
    return vec_result
def vec_sub(vec1, vec2): # вычитание векторов
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem -= vec2[pos]
        vec_result.append(elem)
    return vec_result
def vec_mul(vec1, vec2): # умножить
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem *= vec2[pos]
        vec_result.append(elem)
    return vec_result
def vec_div(vec1, vec2): # делить
    vec_result = []
    for pos, elem in enumerate(vec1):
        elem /= vec2[pos]
        vec_result.append(elem)
    return vec_result
def vec_sqrt(vec): # извлечь корень каждого значения
    for pos, elem in enumerate(vec):
        vec[pos] = math.sqrt(elem)
    return vec
def vec_exponentiation(vec, n): # возвести в степень
    for pos, elem in enumerate(vec):
        vec[pos] = elem**n
    return vec


# операции над всем списком фин.данных
def get_couple_vec(data_list, elem1pos, elem2pos):
    return [data_list[elem1pos], data_list[elem2pos]]
def cng_vec_pos(data_list, pos1, pos2):
    '''
    меняет местами векторы во входящем list'е данных
    '''
    data_list[pos1], data_list[pos2] \
    = data_list[pos2], data_list[pos1]
    return data_list
def sum_vec_to1(vec1, vec2): # суммируем векторы в один
    return vec_sum(vec1, vec2)
def div_vec_to1(vec1, vec2): # получаем отношение одного вектора к другому
    return vec_div(vec1, vec2)