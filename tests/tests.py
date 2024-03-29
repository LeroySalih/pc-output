"""
level-1::output
"""

from testengine import *
from subprocess import run


from main import *

import random

class MainTestEngine (TestEngine):

    def __init__(self, label):
        super().__init__(label);

    #Check a Def Exists
    
    # def test_def_exists(self):
    #    self.assertDefExists("IsValid_Choice")
    

    #Check the result of a def

    # def IsValid_UserChoice_Y(self):
    #     result = IsValid_Choice("Y")
    #     expected = True
    #     self.assertEqual( expected, result, f"\nExpected: {expected}.\nReceived:{result}")

    
    #Check the output

    # def test_output_is_correct(self): 
    #   user_input=b"A\ny\nn\Y"    
    #   result = run(["python", "main.py"], input=user_input, capture_output=True)
        
    #   expected = b"Enter a choice (Y/N)Incorrect choice, try again.\nEnter a choice (Y/N)Incorrect choice, try again.\nEnter a choice (Y/N)Incorrect choice, try again.\nEnter a choice (Y/N)"

    #   self.assertEqual(expected,  result.stdout, "\nExpected:\n{0}\nReceived:\n{1}".format(expected, result.stdout))

    def test_output_is_correct(self): 
      user_input=b""

      result = run(["python", "main.py"], input=user_input, capture_output=True)
        
      expected = b'Hello World\n15\n\xf0\x9f\x91\x8c\n'

      self.assertEqual(expected,  result.stdout, "\nExpected:\n{0}\nReceived:\n{1}".format(expected, result.stdout))

      


    def getTests(self):
        return [
          self.test_output_is_correct
        ]