from pymongo import MongoClient
import threading

thread_local = threading.local()


def get_mongo_client():
    # from django.conf import settings

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
    for key, value in get_request.items():
        if value!='' and key!='csrfmiddlewaretoken':
            qs.update({key:value})
    return qs
