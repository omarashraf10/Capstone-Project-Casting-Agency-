Capstone Project for FSND Full Stack Developer Nanodegree

### Base URL
https://evening-chamber-56051.herokuapp.com/

### Motivations
final project of full stack nanodegree ipmroves my skills and teaches lots of topics

## Getting Started

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


#### Database Setup

 
for my local postgres path :'postgresql://postgres:Email1085@localhost:5432/agency'
for my postgres on heroku :
"postgres://ylaxdrdccwkyfc:da1f14f338d94932f33905dedd4ce95aad945755897d2cdc4a2755e0c4ce468c@ec2-18-208-102-44.compute-1.amazonaws.com:5432/d68n857frnfinv"

change with your database path in brackets below
database_path = "postgres://{}:{}@{}/{}".format(<user-name>,'<password>','localhost:5432', <database_name>)"

## Running the server

From within the `Capstone-Project-Casting-Agency-` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### Tasks

## Endpoints and error handlung
Creating company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for actors and movies 
3. Create an endpoint to DELETE actors and movies using their ID. 
4. Create an endpoint to POST a new actor and new movie
5. Create a PATCH endpoint to patch actors and movies based on their IDs. 
6. Create error handlers for all expected errors including 400, 404, 422 and 405.

### Setup Auth0

1. Create a new, single page web application
2. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
3. Create new API permissions:
    -add:actors
    -add:movies
    -delete:actors
    -delete:movies
    -get:actors
    -get:movies
    -patch:actors
    -patch:movies

4. Create new roles for:
    - Casting Assistant
        -get:actors
        -get:movies
    - Casting Director
        -get:actors	
        -get:movies
        -delete:actors
        -create:actors
        -patch:movies
        -patch:actors
    - Executive Producer   	
        can perform all actions

5. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 3 users
    - Sign into each account and make note of the JWT.
    - add your token in authorization tab 
    - for test cases you can just add to your endpoint a header with 
      " Bearer ......(your noted token)"



### End Points

GET /actors
Request Headers: None
Requires permission: read:actors
Using Postman with sample below and curl
Sample: curl -X GET https://evening-chamber-56051.herokuapp.com/actors

    {
    "actors":[
        {
            "age":60,
            "gender":"male",
            "id":1,
            "name":"Omar"
        }
    ],
    "success":True
}
GET /movies
Request Headers: None
Requires permission: read:movies
Using Postman with sample below
Sample: curl -X GET https://evening-chamber-56051.herokuapp.com/movies

 {
   "movies":[
      {
        "id":1,
        "title": ""eljazera"",
        "release_date": "2007-08-09",
        "genre": "Action"
      }
   ],
   "success":True
}

DELETE /actors/actor_id
Request Arguments: integer id
Request Headers: None
Requires permission: delete:actors
Using Postman with sample below
Sample: curl -X DELETE https://evening-chamber-56051.herokuapp.com/actors/2

    {
    "deleted": 2,
    "success": true
}

DELETE /movies/movie_id
Request Arguments: integer id
Request Headers: None
Requires permission: delete:movies
Using Postman with sample below
Sample: curl -X DELETE https://evening-chamber-56051.herokuapp.com/actors/1

  {
    "deleted": 1,
    "success": true
}


POST /actors
Request Arguments: None
Request Headers: (application/json) string name - integer age - string gender
Requires permission: create:actors
Using Postman with sample below
Sample: curl -X POST https://evening-chamber-56051.herokuapp.com/actors

    {
    "actor_id": 3,
    "success": true
}

POST /movies
Request Arguments: None
Request Headers: (application/json) string title - date release_date
Requires permission: create:movies
Using Postman with sample below
Sample: curl -X POST https://evening-chamber-56051.herokuapp.com/movies

    {
    "movie_id": 2,
    "success": true
}

PATCH /actors/actor_id
Request Arguments: integer id
Request Headers: (application/json)  string name - integer age - string gender
Requires permission: edit:actors
Using Postman with sample below
Sample: curl -X PATCH https://evening-chamber-56051.herokuapp.com/actors/3

{
   "actor":{
      "age":60,
      "gender":"male",
      "id":3,
      "name":"Ahmed"
   },
   "success":True
}
PATCH /movies/movie_id
Request Arguments: integer id
Request Headers: (application/json)  string title - date release_date
Requires permission: edit:movies
Using Postman with sample below
Sample: curl -X PATCH https://evening-chamber-56051.herokuapp.com/movies/1

{
   "movie":{
      "genre":"Action",
      "id":1,
      "release_date":"2006-04-12",
      "title":"Tito"
   },
   "success":True
}
### Login URL
https://omarfsnd.us.auth0.com/authorize?audience=Agency&response_type=token&client_id=q4QdKKOAt1lmC1kAvmF1vAepCiWdBfzM&redirect_uri=https://evening-chamber-56051.herokuapp.com/

### Users
# Casting Assistant
 UserAssistant@yahoo.com
 AssistantPassword123
# Casting Director
 UserDirector@yahoo.com
 DirectorPassword123
# Executive Producer
 UserProducer@yahoo.com
 ProducerPassword123
 
### Unit tests 

 to run test cases   
 
 setup the environment variable
 
 export AUTH0_DOMAIN = 'omarfsnd.us.auth0.com'

 export API_AUDIENCE = 'Agency'
 
 export ALGORITHMS = ['RS256']
 
 export FLASK_APP=flaskr
 
 export FLASK_ENV=development
 
 export DATABASE_URL="postgres://ylaxdrdccwkyfc:da1f14f338d94932f33905dedd4ce95aad945755897d2cdc4a2755e0c4ce468c@ec2-18-208-102-44.compute-1.amazonaws.com:5432/d68n857frnfinv"

 export ASSISTANT_TOKEN=''
 
 export DIRECTOR_TOKEN=''
 
 export PRODUCER_TOKEN=''

 use this command 
$ python test_flaskr.py
....................
----------------------------------------------------------------------
Ran 20 tests in 6.939s

OK
