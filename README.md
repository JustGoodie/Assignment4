Gamess4Geeks Gamess4Geeks - is a program that outputs the results of the minimum or recommended system requirements of the game as you enter the game name in the search field. The information is sent to the database using an API request of GameReqsAPI and then the information is displayed on the site. The program itself runs in Python. Connecting to a Postgres database (Pg admin4). We also use html, css, bootstrap for the site.

Installation Python: Install the current version of Python: PyCharm Version: 2022.2.3 Assembly: 222.4345.23 October 16, 2022 Postgres: Pg Admin 4 Version 6.1 (4280.88) Terminal in PyCharm:

pip install psycopg2 pip install flask pip install requests pip install flask-request

In PgAdmin4: Open the PostgreSQL 13 and CREATE NEW DATABASE and CALL IT "PyProject_db"". Open the PyProject_db database >>> Schemas >>> Tables >> right mouse button and click Query Tool >>> Query Editor >>> Paste it: CREATE TABLE recommended (ID SERIAL PRIMARY KEY not NULL, G_NAME TEXT , CPU VARCHAR(600), RAM VARCHAR(600), GPU VARCHAR(600), DX VARCHAR(600), OS VARCHAR(600), Store VARCHAR(600))

and

CREATE TABLE minimal (ID SERIAL PRIMARY KEY not NULL, G_NAME TEXT , CPU VARCHAR(600), RAM VARCHAR(600), GPU VARCHAR(600), DX VARCHAR(600), OS VARCHAR(600), Store VARCHAR(600))

Usage Spec It API Documentation:

const axios = require("axios");

const options = { method: 'GET', url: 'https://spec-it.p.rapidapi.com/batman-arkham-city', headers: { 'X-RapidAPI-Key': '79e45bf277msh84f2840e7a48c1dp1fed2bjsnd23c661c5706', 'X-RapidAPI-Host': 'spec-it.p.rapidapi.com' } };

axios.request(options).then(function (response) { console.log(response.data); }).catch(function (error) { console.error(error); });

Examples for use: Run main.py. Click localhost in terminal, and and the program will open your browser. You need to type name of the game and choose recommended or minimal requirements and then click "Search". After clicking on the site, information about your relevant requirements that you have chosen earlier will be displayed.

image

image
