import logging
import time
from common.config import DEFULT_INDEX
from indexer.index import tair_vector_client, count_collection


def do_count(index_name):
    if not index_name:
        index_name = DEFULT_INDEX
    try:
        index_client = tair_vector_client()
        num = count_collection(index_client, index_name)
        return num
    except Exception as e:
        logging.error(e)
        return "Error with {}".format(e)