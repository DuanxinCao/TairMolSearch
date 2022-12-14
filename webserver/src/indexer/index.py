import logging
from common.config import *
import redis
from tair.tairvector import TairVectorCommands as TairVector
from tair import Tair

client = Tair(host=TAIR_VECTOR_HOST, port=TAIR_VECTOR_PORT,password=TAIR_PASSWOED)

def tair_vector_client():
    try:
        #client = TairVector(redis.Redis(host=TAIR_VECTOR_HOST, port=TAIR_VECTOR_PORT))
        logging.info("host %s, port %s" %(TAIR_VECTOR_HOST, TAIR_VECTOR_PORT))
        return client
    except Exception as e:
        print("TairVector ERROR:", e)
        logging.error(e)


def knn_search(client, index_name, vectors, top_k):
    try:
        result = client.tvs_knnsearch(index_name,top_k, vectors)
        return result
    except Exception as e:
        print("TairVector Search ERROR:", e)
        logging.error(e)


def count_collection(client, index_name):
    try:
        index = client.tvs_get_index(index_name)
        if index is None:
            print("index %s not exist" % index_name)
            return -1
        return int(index.get('data_count'))
    except Exception as e:
        print("TairVector ERROR:", e)
        logging.error(e)
        
        
def get_attr(client, index_name, key, attr_key):
    try:
        result = client.tvs_hmget(index_name, key, attr_key)
        return result
    except Exception as e:
        print("TairVector hmget ERROR:", e)
        logging.error(e)