from pymongo import MongoClient
import threading
import re

thread_local = threading.local()


def get_mongo_client():

    client = thread_local.__dict__.get('mongo_client', None)

    if client is None:
        try:
            client = MongoClient('mongodb://localhost:27017/')
        except Exception as e:
            print e
            thread_local.mongo_client = None
    else:
        thread_local.mongo_client = client
    return client


def get_mongo_database():
    import settings
    client = get_mongo_client()
    return client[settings.MONGO_DATABASE] if client else None


def get_params_from_request(get_request):
    qs = {}
    name = 'name'
    for key, value in get_request.items():
        if value != '' and key != 'csrfmiddlewaretoken' and key != 'page':
            if name == key:
                qs.update({key: value})
            else:
                if len(re.findall("_to", key)) > 0:
                    newkey = key[0:-1]
                    newvalue = qs.get(newkey, '')
                    if newvalue == '':
                        addparam = {key: {"$lt": value}}
                        qs.update(addparam)
                    else:
                        newvalue.update({"$lt": value})
                else:
                    newvalue = qs.get(key, '')
                    if newvalue == '':
                        addparam = {key: {"$gt": value}}
                        qs.update(addparam)
                    else:
                        newvalue.update({"$gt": value})
    return qs
