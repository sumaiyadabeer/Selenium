import pytest
#from selenium import webdriver
@pytest.yield_fixture()
def setup():
	print("opening URL")
	yield
	print("closing browser after login")


def test_loginByEmail(setup):
	print("this is login by email test")
	
def test_loginByFacebook(setup):
	print("this is login by facebook test")
	


