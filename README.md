#Games4Geeks
Games4Geeks - is a program that outputs the results of the minimum or recommended system requirements of the game as you enter the game name in the search field.
The information is sent to the database using an API request of GameReqsAPI and then the information is displayed on the site. 
The program itself runs in Python. Connecting to a Postgres database (Pg admin4). We also use html, css, bootstrap for the site.

Installation
Python: Install the current version of Python: PyCharm
Version: 2022.2.3 Assembly: 222.4345.23 October 16, 2022
Postgres: Pg Admin 4
Version 6.1 (4280.88)
Terminal in PyCharm:

pip install psycopg2
pip install flask
pip install requests
pip install flask-request

In PgAdmin4:
Open the PostgreSQL 13 and add a new table to a existing database and call it users:  

CREATE TABLE users (
  id serial PRIMARY KEY,
  fullname VARCHAR ( 100 ) NOT NULL,
  username VARCHAR ( 50 ) NOT NULL,
  password VARCHAR ( 255 ) NOT NULL)

Usage
Spec It API Documentation:

const axios = require("axios");

const options = {
  method: 'GET',
  url: 'https://spec-it.p.rapidapi.com/batman-arkham-city',
  headers: {
    'X-RapidAPI-Key': '79e45bf277msh84f2840e7a48c1dp1fed2bjsnd23c661c5706',
    'X-RapidAPI-Host': 'spec-it.p.rapidapi.com'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});


Examples for use:
Run main.py.
Click localhost in terminal, and and the program will open your browser. First of all, you will need to log in. If you
do not authorised in this website, you will have to register. And then only you can search games.
After you logged in, you need to type name of the game and choose recommended or minimal requirements and then click "Search".
After clicking on the site, information about your relevant requirements that you have chosen earlier will be displayed.

Team of the project:
Nurbek Naiman
Ertuar Yerkebulan

![image](https://user-images.githubusercontent.com/92390698/198972245-1701b8ec-fd18-40a7-bbea-60fb66558287.png)
![image](https://user-images.githubusercontent.com/92390698/198972298-9a03c5a5-0d14-4b16-8e14-5a35f93bc71e.png)
![image](https://user-images.githubusercontent.com/92390698/198972340-0e327ca7-0cf5-44a9-b109-d16df94da0a4.png)
![image](https://user-images.githubusercontent.com/92390698/198972444-b42826cf-700a-4d5a-bc45-d196ddd14da1.png)

