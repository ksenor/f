# -*- coding: utf-8 -*-

import unittest as ut

import primitives as p

class DataLoaderTester(ut.TestCase):

    def setUp(self):
        '''
        тестирование правильной работы примитивов
        '''
        
        self.primitive = p
    
    def test_basic_primitives(self):
        '''
        все базовые математические операции над 
        одним, или несколькими аргументами
        '''
        # плюс
        self.assertEqual(self.primitive.add(1,2), 3)
        # минус
        self.assertEqual(self.primitive.sub(3,1), 2)
        # умножить
        self.assertEqual(self.primitive.mul(2,3), 6)
        # делить
        self.assertEqual(self.primitive.div(6,3), 2)
        # корень
        self.assertEqual(self.primitive.sqrt(100), 10)
        # степень
        self.assertEqual(self.primitive.exponentiation(10, 2), 100)
        # первый из ..
        self.assertEqual(self.primitive.first_elem([1,2,3]), 1)
        # последний из ..
        self.assertEqual(self.primitive.last_elem([1,2,3]), 3)
        # заданный элемент из множества
        self.assertEqual(self.primitive.any_elem([1,2,3], 1), 2)

    def test_vec_opers(self):
        '''
        все базовые математические операции над 
        одним, или несколькими векторами
        '''
        # плюс
        self.assertEqual(self.primitive.vec_sum([1,2], [4,3]), [5,5])
        # минус
        self.assertEqual(self.primitive.vec_sub([1,2], [1,2]), [0,0])
        # умножить
        self.assertEqual(self.primitive.vec_mul([1,2], [2,3]), [2,6])
        # делить
        self.assertEqual(self.primitive.vec_div([6,3], [2,3]), [3,1])
        # корень каждого из значений
        self.assertEqual(self.primitive.vec_sqrt([100, 49]), [10, 7])
        # степень - = -
        self.assertEqual(self.primitive.vec_exponentiation(
                            [10, 3], 2), [100, 9])

    def test_list_data_opers(self):
        # получаем из всего списка пару векторов
        self.assertEqual(self.primitive.get_couple_vec(
                            [[1,2,3], [3,1,2], [5,1,2]], 0, 2),
                            [[1,2,3], [5,1,2]])
        # меняем местами векторы
        self.assertEqual(self.primitive.cng_vec_pos(
                            [[1,2], [3,4]], 0, 1), [[3,4], [1,2]])
        # складываем 2 вектора в 1
        self.assertEqual(self.primitive.sum_vec_to1(
                            [1,2], [3,4]), [4,6])
        # делим один вектор на другой 
        self.assertEqual(self.primitive.div_vec_to1(
                            [3,49,100],[3,7,10]), [1,7,10])
        
        
if __name__ == '__main__':
    ut.main()