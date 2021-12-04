import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr.database.models import setupDB,createAll, Movie, Actor
from flaskr import createApp
import datetime

#TEST_DATABASE_URI = os.getenv('DATABASE_URL')
#ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
#DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
#PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')
TEST_DATABASE_URI = 'postgresql://ylaxdrdccwkyfc:da1f14f338d94932f33905dedd4ce95aad945755897d2cdc4a2755e0c4ce468c@ec2-18-208-102-44.compute-1.amazonaws.com:5432/d68n857frnfinv'
ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InQzSGZfeWtxSGp3QmEwWFFiVi1fUCJ9.eyJpc3MiOiJodHRwczovL29tYXJmc25kLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWFhNDA2NjA4MzkzMTAwNmFjNDA0ZGUiLCJhdWQiOiJBZ2VuY3kiLCJpYXQiOjE2Mzg2MjgwOTksImV4cCI6MTYzODYzNTI5OSwiYXpwIjoicTRRZEtLT0F0MWxtQzFrQXZtRjF2QWVwQ2lXZEJmek0iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.dlLhc0GnO5Ruf8FFuF--YKWrXM7h8gLq-eP40CXq7xcLGx0zkoIlcphDDJX8bkN__OVvx_ZGEpsR1W1Lyfx1SqY3igE7xS9JE-XgSB6bKqPp7hnS3PQgSOiWqYfYRG6FJIZHbZ64BqyEJecRV2aYjZ1SQwvxvKXWsaSbZq1sNnaXVme5sYXrP3cXscYibIk3o6g8rzNMSMxX-qMapA6ofReYjiQGQtPLZYZHifI2xHqPj26WkAwCdUp4cLlcvseJ0vbC9ccLIY6_3nSACbZsg3xhGBnjakQYbnMrjErmBYNYTUPxYlWpgrfzosVa2c7qVjANj59ZFQt-ZtaU3ZYwjA'
DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InQzSGZfeWtxSGp3QmEwWFFiVi1fUCJ9.eyJpc3MiOiJodHRwczovL29tYXJmc25kLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWFhNDBhYTY3OGEwYzAwNjg5NDQ4OTMiLCJhdWQiOiJBZ2VuY3kiLCJpYXQiOjE2Mzg2MjgxNzYsImV4cCI6MTYzODYzNTM3NiwiYXpwIjoicTRRZEtLT0F0MWxtQzFrQXZtRjF2QWVwQ2lXZEJmek0iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiXX0.QcO9y5ZpqqabIL4XpLVK7dkYDjtJ4VM9OxbwASPkIHRLqF_a-iO9nPButomHReXcXxZwxmqaMKyVZcTSH1yzfVGqeLGXkNWKJxo-9VrHiN0fTU4e7ESfW31KPih2Ln45pxTy5n1wE3LqIeO2cxL1bCOOP5eQA9Al_U2EqqYcs6rF33Dp4J1ld3VCAsoF3uglAZhDTT1CvFHFPVGsO2sLQaUFqj7Kbhg3Ox8txyYDx-RoxhnLhIa-tLAxaLEgyVkZsRKl561-Lq3da7Ca3CWvS3WrkyKxnQ-yTpuA8y1fjZbQZfaYqf6LgT0_p-RNB-x_Ld_yP41fY8etiddb1uiABQ'
PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InQzSGZfeWtxSGp3QmEwWFFiVi1fUCJ9.eyJpc3MiOiJodHRwczovL29tYXJmc25kLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWFhNDBlZjY3OGEwYzAwNjg5NDQ4YzEiLCJhdWQiOiJBZ2VuY3kiLCJpYXQiOjE2Mzg2MjgyODEsImV4cCI6MTYzODYzNTQ4MSwiYXpwIjoicTRRZEtLT0F0MWxtQzFrQXZtRjF2QWVwQ2lXZEJmek0iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyJdfQ.yUsnWIj_uhv-1SYZEy25XIV6ni7wTRsMTkjMZS_N2b19oLpee9CI8UH6EG2umf_0hX_AkZKhHi0B9zyUcAqxdCuelVRoTZ3aXFir29IzmzTVG1sMR0CGP8EKWYrQRJZNFlTjpcOYgOyL5uU6Bl1Jj3YnPoVnWU15mzkCPMeDoiu9jNrVyLWwEsVtyTkJthOHVVKQ-JDn4JViS4BzzW94icFMnFhvSdHAbSVXCpZtUoWohySGSjVMrLcl7w2IaHCxMHr2wUTuVOEZU4b7G4dzHx-KhPzFLfA-lSrTxOh-63FJrg66lLU2CMizwYikvQNHY2_gbJY0bp73pwXeoRKx1A'

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = createApp()
        self.client = self.app.test_client
        setupDB(self.app, TEST_DATABASE_URI)
        self.casting_assistant = ASSISTANT_TOKEN
        self.casting_director = DIRECTOR_TOKEN
        self.executive_producer = PRODUCER_TOKEN
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            createAll()

    def tearDown(self):
        """Executed after reach test"""
        pass
    
    
    def testGetActors(self):
        actor=Actor(name='Omar',
                    age=60,
                    gender='male')
        actor.insert()
        res=self.client().get('/actors',
                              headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def testPostActorsCastingDirector(self):
        actor = {
            "name": "Ahmed",
            "gender": "male",
            "age": 70
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.casting_director)
                                 }, json=actor)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        actor_db  = Actor.query.get(data['actor_id'])
        actor['id'] = data['actor_id']
        self.assertEqual(actor_db .format(), actor)

    def testPostActorsCastingAssistant(self):
        actor = {
            "name": "Mohamed",
            "gender": "male",
            "age": 70
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.casting_assistant)
                                 }, json=actor)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)

    
    def testPatchActorProducer(self):
        actor=Actor(name='Fawzy',
                    age=60,
                    gender='male')
        actor.insert()#so we have at least one Actor
        
        actor_patch = {
            "gender": "male",
            "age": 70
        }

        res = self.client().patch('/actors/'+str(actor.id),
                                  headers={
            "Authorization": "Bearer {}".format(self.executive_producer)
        }, json=actor_patch)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(200, res.status_code)
        actor = Actor.query.get(data['actor']['id'])
        actor_json = actor.format()
        for key in actor_patch.keys():
            self.assertEqual(actor_patch[key], actor_json[key])

    def testPatchActorCastingAssistant(self):
        actor=Actor(name='Mustafa',
                    age=60,
                    gender='male')
        actor.insert()#so we have at least one Actor
        
        actor_patch = {
            "gender": "male",
            "age": 70
        }

        res = self.client().patch('/actors/'+str(actor.id),
                                  headers={
            "Authorization": "Bearer {}".format(self.casting_assistant)
        }, json=actor_patch)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)



    def testDeleteActor(self):
        actor=Actor(name='Omar',
                    age=60,
                    gender='male')
        actor.insert()#so we have at least one Actor
        
        res = self.client().delete('/actors/'+str(actor.id),
                                    headers={
            "Authorization": "Bearer {}"
            .format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        actor = Actor.query.get(data['deleted'])
        self.assertEqual(actor, None) 

    def testPostActorFail400(self):
        actor = {
            "name": "Mohamed",
            "age": 70
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=actor)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(400, res.status_code)
        self.assertNotEqual(len(data['message']), 'Bad request')

    def testGetActorsFails401(self):
        actor=Actor(name='Ahmed',
                    age=60,
                    gender='male')
        actor.insert()
        res=self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def testDeleteActorFail403(self):
        actor=Actor(name='Ahmed',
                    age=60,
                    gender='male')
        actor.insert()#so we have at least one Actor
         
        res = self.client().delete('/actors/'+str(actor.id),
                                    headers={
            "Authorization": "Bearer {}"
            .format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)
        
    def testPatchActorFail404(self):
        actor_patch = {
            "gender": "male",
            "age": 70
        }
        res = self.client().patch('/actors/1000',
                                  headers={
                                      "Authorization": "Bearer {}"
                                      .format(self.casting_director)
                                  }, json=actor_patch)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)
      
    def testPostActorFail400(self):
        actor = {
            "gender": "male",
            "age": 70
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=actor)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(400, res.status_code)
        self.assertNotEqual(len(data['message']), 'Bad request') 
        


    def testGetMovies(self):
        movie=Movie(title='eljazera',
                    release_date=datetime.date.fromisoformat('2007-08-09'),
                    genre='Action')
        movie.insert()
        res=self.client().get('/movies',
                              headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    
    def testPostMoviesProducer(self):
        movie = {
            "title": "eljazera",
            "release_date": "2007-08-09",
            "genre": "Action"
        }

        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=movie)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        movie_db = Movie.query.get(data['movie_id'])
        movie['id'] = data['movie_id']
        self.assertEqual(movie_db.format(), movie)


    def testPostMoviesCastingAssistant(self):
        movie = {
            "title": "eljazera",
            "release_date": "2007-08-09",
            "genre": "Action"
        }

        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.casting_assistant)
                                 }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)


    def testPatchMovieProducer(self):
        movie=Movie(title='eljazera',
                    release_date=datetime.date.fromisoformat('2007-08-09'),
                    genre='Action')
        movie.insert()#so we have at least one movie
        movie_patch = {
            "title": "Ibraheem Elabyd",
            "release_date": "2019-11-02",
        }

        res = self.client().patch('/movies/'+str(movie.id),
                                  headers={
            "Authorization": "Bearer {}".format(self.executive_producer)
        }, json=movie_patch)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(200, res.status_code)
        movie = Movie.query.get(data['movie']['id'])
        movie_json = movie.format()
        for key in movie_patch.keys():
            self.assertEqual(movie_patch[key], movie_json[key])

    def testPatchMovieCastingAssistant(self):
        movie=Movie(title='eljazera',
                    release_date=datetime.date.fromisoformat('2007-08-09'),
                    genre='Action')
        movie.insert()#so we have at least one movie
        movie_patch = {
            "title": "Ibraheem Elabyd",
            "release_date": "2019-11-02",
        }

        res = self.client().patch('/movies/'+str(movie.id),
                                  headers={
            "Authorization": "Bearer {}".format(self.casting_assistant)
        }, json=movie_patch)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)
    

    def testDeleteMovie(self):
        movie=Movie(title='eljazera',
                    release_date=datetime.date.fromisoformat('2007-08-09'),
                    genre='Action')
        movie.insert()#so we have at least one movie

        res = self.client().delete('/movies/'+str(movie.id),
                                    headers={
            "Authorization": "Bearer {}"
            .format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        movie = Movie.query.get(data['deleted'])
        self.assertEqual(movie, None) 

    def testPostMoviesFail400(self):
        movie = {
            "release_date": "2019-11-02",
            "genre": "Action"
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(400, res.status_code)
        self.assertNotEqual(len(data['message']), 'Bad request')

    def testGetMoviesFails401(self):
        movie=Movie(title='eljazera',
                    release_date=datetime.date.fromisoformat('2007-08-09'),
                    genre='Action')
        movie.insert()
        res=self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def testDeleteMovieFail403(self):
        movie=Movie(title='eljazera',
                    release_date=datetime.date.fromisoformat('2007-08-09'),
                    genre='Action')
        
        movie.insert()#so we have at least one movie
        print("aaaaa"+str(movie.id))    
        res = self.client().delete('/movies/'+str(movie.id),
                                    headers={
            "Authorization": "Bearer {}"
            .format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)
        
    def testPatchMovieFail404(self):
        movie = {
            "title": "movie1",
            "release_date": "2005-02-02",
        }
        res = self.client().patch('/movies/1000',
                                  headers={
                                      "Authorization": "Bearer {}"
                                      .format(self.casting_director)
                                  }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)
      
    def testPostMoviesFail400(self):
        movie = {
            "title": "movie2",
            "release_date": "2017-01-12",
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.executive_producer)
                                 }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(400, res.status_code)
        self.assertNotEqual(len(data['message']), 'Bad request') 
        
if __name__ == "__main__":
    unittest.main()