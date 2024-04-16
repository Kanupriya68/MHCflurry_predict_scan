import csv
import main
import unittest

class mhcflurry_Test_Class(unittest.TestCase):
   def test_header(self):
       #Checks whether data is populated or not
       return_value = main.mhcflurry("MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVL", "HLA-A*02:01")
       self.assertTrue(return_value[0])
   def test_csv_rows(self):
       #Checks whether data is populated or not
       return_value = main.mhcflurry("MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVL", "HLA-A*02:012")
       self.assertTrue(return_value[1:])


# i will use code below to run the unit test
t = mhcflurry_Test_Class()
suite = unittest.TestLoader().loadTestsFromModule(t)
unittest.TextTestRunner().run(suite)