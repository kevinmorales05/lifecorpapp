
from main import *
import pytest

numPersons = 3
fixedCosts =  [
        {
          "cost": "1700",
          "costDescription": "1700",
          "costName": "Flight ticket",
          "quantity": "1"
        },
        {
          "cost": "1050",
          "costDescription": "refugee visa",
          "costName": "Visa",
          "quantity": "1"
        }
      ]
variableCosts = [
        {
          "cost": "30",
          "costDescription": "breakfast, lunch, dinner",
          "costName": "Food",
          "quantity": "7"
        },
        {
          "cost": "20",
          "costDescription": "extra activities to discover the city",
          "costName": "Amusement",
          "quantity": "4"
        },
        {
          "cost": "70",
          "costDescription": "flight seoul to busan",
          "costName": "Inter flight",
          "quantity": "1"
        }
      ]

# User in the firebase database
NIJLfM3DjXH0PSGBPy = {
      "email": "kmorales@com.com",
      "name": "Kevin Morales",
      "pwd": "12345"
    }

def test_getTotalCostPerPerson():
    assert getTotalCostPerPerson(numPersons, fixedCosts, variableCosts) == 2870

def test_loginWithFirebase():
    #Negative Result
    assert loginWithFirebase(NIJLfM3DjXH0PSGBPy['email'], "incorrectpwd") == 'No'
    #Positive Result
    assert loginWithFirebase(NIJLfM3DjXH0PSGBPy['email'],NIJLfM3DjXH0PSGBPy['pwd'] ) == NIJLfM3DjXH0PSGBPy

def test_isValidEmail():
    assert isValid("fakeemail") == False
    assert isValid("truemeail@gmail.com") == True
    assert isValid("almostTru@gmail") == False

pytest.main(["-v", "--tb=line", "-rN", __file__])