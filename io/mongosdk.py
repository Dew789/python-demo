import pymongo


def get_db():
    client = pymongo.MongoClient("mongodb://mongodb:mongodb@192.168.127.138:27017/")
    db = client["practice"]
    return db


def get_collection(db):
    collection = db["SystemObject"]
    return collection


def insert_one_doc(collection):
    information = {"name": "quyang", "age": "25"}
    information_id = collection.insert(information)


def insert_multi_docs(collection):
    information = [{"name": "mike", "age": "25"}, {"name": "janedoe", "age": "24"}]
    information_id = collection.insert(information)


def get_one_doc(collection):
    print(collection.find_one())
    print(collection.find_one({"name":"yuiki"}))
    print(collection.find_one({"name":"pppp"}))


def get_one_by_id(collection):
    obj = collection.find_one()
    obj_id = obj["_id"]
    # print(collection.find_one({"_id":obj_id})
    str_obj_id = str(obj_id)

    from bson.objectid import ObjectId 
    # print(collection.find_one({"_id":ObjectId(str_obj_id)}))


def get_many_docs(collection):
    count = collection.count()
    count_condition = collection.find({"name":"quyang"}).count()
    for item in collection.find().sort("age", pymongo.DESCENDING):
        print(item)


def clear_all_data(collection):
    collection.remove()


if __name__ == '__main__':
    db = get_db()
    collection = db["ppp"]
