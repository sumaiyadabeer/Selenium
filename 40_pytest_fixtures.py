
import pytest

@pytest.fixture()
def setupo():
	print("before")

@pytest.yield_fixture()
def setup():
	print("once before every method")
	yield
	print("once after every method")



def testMethod1(setup,setupo):
	print("this is test method 1")

def testMethod2(setup,setupo):
	print("this is test method 2")
	




