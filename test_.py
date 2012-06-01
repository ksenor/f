# -*- coding: utf-8 -*-

import unittest as ut

import f

class DataLoaderTester(ut.TestCase):

    def setUp():
        '''
        
        '''
        dl = f.DataLoader('eurgpb.txt')
    
    def test_load_data():
        '''
        правильные данные - на выходе матрица значений, 
        из одного большого списка, и много маленьких, вложенных:
        [
            [],
            [],
            [],
            ...
        ] где количество элементов в каждом из них, 
        по одной и той же валютной паре, только одинаковое.
        + одинаковой должна быть и разрядность элементов каждого 
        вектора(кол-во элементов в строке любого из значений
        вектора, равно количеству элементов произвольного
        значения, из того же ряда)
        '''
        loaded = dl.load_data()
        self.assertEqual(type(loaded), type([]))
        self.assertEqual(type(loaded[0], type([]))