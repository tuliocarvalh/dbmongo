import pymongo
from pymongo import MongoClient
from pass_ import *
import random
password = password()
url = f""
cluster = MongoClient(url)
db = cluster["test"]
collection = db["test"]

###for add 1

#post = {"_id": 0, "name": "tim", "score": 5}
#collection.insert_one(post)

###for add more
#collection.insert_one(falas)
#data1 = {"_id": 1, "name": "joao", "score": 5}
#data2 = {"_id": 2, "name": "pedro", "score": 2}
#collection.insert_many([falas1, falas2, falas3])
#print(cluster.list_database_names())

###for search

def all_nomes() :
    results = collection.distinct("name")
    return results
print(all_nomes())
    


def nomes() :
    nome = input("nome: ")
    nome = f"""{nome}"""
    results = collection.find({"name":nome})
    #results = collection.find({"name":"joao"})
    for resultados in results :
        return resultados
print(nomes())





### for delete

#results = collection.delete_one({"_id":0})
#esults = collection.delete_many({}) #all or {""}+

### for update 

#results = collection.update_one({"_id":0}, {"$set"{"name:"tim}})




