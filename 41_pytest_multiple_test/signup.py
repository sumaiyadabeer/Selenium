import pytest
#from selenium import webdriver
@pytest.yield_fixture()
def setup():
	print("opening URL")
	yield
	print("closing browser after signup")


def test_signupByEmail(setup):
	print("this is signup by email test")
	
def test_signupByFacebook(setup):
	print("this is signup by facebook test")
	


