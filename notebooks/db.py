import pymongo


class DB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://octo_user:Fanta1976@cluster0.ki3lm4v.mongodb.net"
                                          "/?retryWrites=true&w=majority")
        self.db = self.client['TweeterAnalyzeCluster']
    def createCollection(self, collectionName="tweetCollection"):
        self.db.create_collection(collectionName)
    def insert(self, data):
        self.db['tweetCollection'].insert(data)

    def find(self, query):
        return self.db['tweetCollection'].find(query)

    def update(self, query, data):
        self.db['tweetCollection'].update(query, data)

    def delete(self, query):
        self.db['tweetCollection'].remove(query)
