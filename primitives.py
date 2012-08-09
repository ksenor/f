# -*- coding: utf-8 -*-

import math

# примитивы в математике
def add(a, b): return a+b # сложение
def sub(a, b): return a-b # вычитание
def mul(a, b): return a*b # умножение
def div(a,b): return a/b # деление
def sqrt(a): return math.sqrt(abs(a)) # корень
def exponentiation(x, n): return x**n # возведение в степень
    
    
# операции над всем списком фин.данных
def cng_vec_pos(data_list, pos1, pos2):
    '''
    меняет местами векторы во входящем list'е данных
    '''
    data_list[pos1], data_list[pos2] \
    = data_list[pos2], data_list[pos1]


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
# 