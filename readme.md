How to set up and run
1. Update pip
pip install --upgrade pip
2. Install firebase admin
pip install firebase_admin

run python3 main.py


In order to test
1. In the data.json you have information from the Firebase database in order to test login function.

run python3 test.py



*** Database  Collection ***
Users Collection
[
	"UserID1":
	{
		"name": "Kevin Morales",
		"email": "kevin@gmail.com",
		"password": "prueba12345"
	},
	"UserID2":
	{
		"name": "Juan Morales",
		"email": "juan@gmail.com",
		"password": "prueba12345"
	},
    "UserID3":
	{
		"name": "Andres Morales",
		"email": "andres@gmail.com",
		"password": "prueba12345"
	},
    "UserID4":
	{
		"name": "Leonel Morales",
		"email": "leo@gmail.com",
		"password": "prueba12345"
	},
]

*** Products Collection ***

[
	{
		"name":"Work in Korea",
		"description:"Service to help people to find a job in South Korea legally"
		"target": "Adults",
		"fixCost":[{
			"costName":"",
			"costDescription":"",
			"cost":"",
			"quantity":""
		}, {
			"costName":"",
			"costDescription":"",
			"cost":"",
			"quantity":""
		}, {
			"costName":"",
			"costDescription":"",
			"cost":"",
			"quantity":""
		}],
		"variableCosts":[{
			"costName":"",
			"costDescription":"",
			"cost":"",
			"quantity":""
		}, {
			"costName":"",
			"costDescription":"",
			"cost":"",
			"quantity":""
		}, {
			"costName":"",
			"costDescription":"",
			"cost":"",
			"quantity":""
		}],
		"totalCostPerPerson":"",
		"minimunPersonsForProfit":""
	}
]