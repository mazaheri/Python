from pymongo import MongoClient


class MongoDatabase:
    
    def __init__(self):
        self.client = MongoClient()
        self.database = self.client['crawler']