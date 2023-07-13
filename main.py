import unittest
import calc
# class TestCalc(unittest.TestCase):
#     def test_add(self):
#         a=calc.add(10,20)
#         self.assertEqual(a,30)
class Test(unittest.TestCase):
  def setUp(self):
      print('setup called...')
  def tearDown(self):
      print('teardowm called')
  def test_add(self):
      print('test -1 called...')
      a=calc.add(10,20)
      self.assertEqual(a,30)
  def test_sub(self):
      print('test-2 called...')
      a=calc.sub(20,5)
      self.assertEqual(a,15)
  def test_mul(self):
      print('test-2 called...')
      a=calc.mul(20,5)
      self.assertEqual(a,100)
  def test_div(self):
      print('test-2 called...')
      a=calc.div(30,2)
      self.assertEqual(a,15)





    # def test_add(self):
    #
    #     self.assertEqual(calc.add(10,20) ,30)
    # def test_sub(self):
    #     self.assertEqual(calc.sub(30,20),10)
    # def test_mul(self):
    #     self.assertEqual(calc.mul(3,4),12)
    # def test_div(self):
    #     self.assertEqual(calc.div(10,0),5)

if __name__=='__main__':
    unittest.main()