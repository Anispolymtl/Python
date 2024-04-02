import unittest
from unittest import TestCase
from fonctions_a_tester import fizz_buzz, resoudre_equation 


class TestFizzBuzz(TestCase):
    def test_fizz_buzz_3(self):
        # TODO Tester avec un multiple de 3
        assert fizz_buzz(12) == "fizz"       

    def test_fizz_buzz_5(self):
        # TODO Tester avec un multiple de 5
        assert fizz_buzz(10) == "buzz"
        

    def test_fizz_buzz_3_5(self):
        # TODO Tester avec un multiple de 3 et 5
        assert fizz_buzz(15) == "fizzbuzz"
        

    def test_fizz_buzz_non_facteur(self):
        # TODO Tester avec un nombre qui nombre'a pas 3 et 5 comme facteur
        #  et assurez-vous que la valeur en sotie soit une string
        self.assertIsInstance(fizz_buzz(8),str) 
        


class TestResoudreEquation(TestCase):
    def test_resoudre_equation_sans_racine(self):
        # TODO Tester avec un polynome sans racines réelles
        #  et assurez-vous que la valeur en sortie est None
        assert resoudre_equation(2,-1,3) == None
        

    def test_resoudre_equation_une_racine(self):
        # TODO Tester avec un polynome avec une seule solution
        assert resoudre_equation(4,4,1) == -1/2
        

    def test_resoudre_equation_deux_racine(self):
        # TODO Tester avec un polynome avec deux solutions
        assert resoudre_equation(1,-3,-10) ==  (5.0,-2.0) 
        


if __name__ == '__main__':
    unittest.main()
