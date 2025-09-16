import math
import unittest
from calculoIntegral import integral 

class TesteIntegral(unittest.TestCase):
    def test_polinomio(self):
        # Integral de x ao quadrado com intervalos de 0 a 1 = 1/3 (o valor esperado)
        self.assertAlmostEqual(integral("x**2", 0, 1), 1/3, places=5) # 5 casas de precisão

    def test_polinomio2(self):
        self.assertAlmostEqual(integral("3*x**3 - 2*x**2 + 4*x - 1", 0, 1), 13/12, places=5)

    def test_seno(self):
        self.assertAlmostEqual(integral("sin(5*x)", 0, math.pi), 2/5, places=5)

    def test_logaritmo(self):
        self.assertAlmostEqual(integral("log(x+1)", 0, 2), 3*math.log(3) - 2, places=5) #esse log corresponde ao ln.
    
    def test_exponencial(self):
        self.assertAlmostEqual(integral("exp(x)", 0, 1), math.e - 1, places=5)
   
    def test_exp_soma(self):
        self.assertAlmostEqual(integral("exp(x) + x", 0, 1), (math.e - 1) + 0.5, places=5)
    

if __name__ == "__main__":
    unittest.main()
