import unittest

def area(a,b):
    return a*b;

def perimeter(a,b):
    return 2*(a+b);

class RectangleTestCase(unittest.TestCase):
    def test_area_by_zeros(self):
        res = area(0,0)
        self.assertEqual(res,0)

    def test_area_by_zero_and_nozero(self):
        res = area(0,7)
        self.assertEqual(res,0)

    def test_perimeter_by_zeros(self):
        res = perimeter(0,0)
        self.assertEqual(res,0)

    def test_perimeter_by_zero_and_nozero(self):
        res = perimeter(4,0)
        self.assertEqual(res,8)
    
    def test_area_by_two_ones(self):
        res = area(1,1)
        self.assertEqual(res,1)

    def test_area_by_one_and_nonone(self):
        res = area(1,7)
        self.assertEqual(res,7)

    def test_area_by_integers(self):
        res = area(2,3)
        self.assertEqual(res,6)

    def test_perimeter_by_integers(self):
        res = perimeter(4,5)
        self.assertEqual(res,18)

    def test_area_by_big_numbers(self):
        res = area(245456675762434234249239423932, 277472347238428482)
        self.assertEqual(res,68107439969144504009087633020218573906661231224)

    def test_perimeter_by_big_numbers(self):
        res = perimeter(23472472347274328429484239493249249,3428492747247284242942734827439)
        self.assertEqual(res,46951801680043151427454364456153376) 

    def test_area_by_square_roots(self):
        res = area(2**(1/2), 2**(1/2))
        self.assertEqual(res, 2)

    def test_perimeter_by_square_roots(self):
        res = perimeter(2**(1/2), 2**(1/2))
        self.assertEqual(res, 4*2**(1/2))

    def test_area_by_floats_(self):
        res = area(0.1, 0.2)
        self.assertAlmostEqual(res, 0.02)

    def test_perimeter_by_floats(self):
        res = perimeter(0.1, 0.2)
        self.assertAlmostEqual(res, 0.6)

    
