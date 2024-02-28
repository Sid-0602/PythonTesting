import math
import pytest
import source.shapes as shapes

class TestCircle:
    
    #setup and teardown methods can be used to set up a test and then terminate after test.
    
    #This method is a setup method, which is called before each test method in the test class. 
    #It initializes the self.circle attribute with a Circle object from the shapes module, assuming that module is 
    #imported somewhere in the code.
    def setup_method(self,method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10) # we instantiate a circle object.
        
    #This method is a teardown method, which is called after each test method in the test class. 
    #It's responsible for cleaning up any resources that were set up during test initialization.
    def teardown_method(self,method):
        print(f"Tearing down {method}")
        del self.circle #deleted the object after tests.
        
    
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        
    def test_perimeter(self):
        assert self.circle.perimeter() == math.pi * 2 * self.circle.radius