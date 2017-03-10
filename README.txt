# restAPI
A simple restful API agent to create and retrieve user details to and from a database

Language: Python
Database: sqlite3
framework: flask

Objectives:
  a Create a database with two tables
    a.1 one containing user_id, uname, fname, lname
    a.2 second containing add_id, address
  b Create 3 restful API's to
    b.1 to create user
    b.2 to get all user details
    b.3 to get one specific user details

b.1 (create user):
Method: POST
accepted input: uri params
Tested with postman
uri e.g., http://localhost:500/users?uname=vichary&fname=vishwa&lname=chary&addr=jpnagar,Bangalore,KA
response: 200 ok

b.2 (get all user details):
Method: GET
uri: http://localhost:500/users
response e.g.,
{
  "users": [
    {
      "address": [
        "jpnagar",
        "Bangalore",
        "KA"
      ],
      "fname": "vishwa",
      "lname": "chary",
      "username": "vichary"
    },
    {
      "address": [
        "electroniccity",
        "Bangalore",
        "KA"
      ],
      "fname": "santosh",
      "lname": "chary",
      "username": "sant"
    }
  ]
}

b.3 (get one specific user details)
Method: GET
uri: http://localhost:5000/users/vichary
response e.g.,
{
  "user": {
    "address": [
      "jpnagar",
      "Bangalore",
      "KA"
    ],
    "fname": "vishwa",
    "lname": "chary",
    "username": "vichary"
  }
}
