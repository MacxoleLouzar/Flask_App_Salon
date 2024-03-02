from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['SalonDB']
        
    def get_users_collection(self):
        return self.db['users']