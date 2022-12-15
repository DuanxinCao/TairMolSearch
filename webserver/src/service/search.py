import logging
from indexer.index import tair_vector_client, knn_search, get_attr
from encoder.encode import smiles_to_vec
import time


def do_search(index_name, molecular_name, top_k):
    try:
        feats = []
        index_client = tair_vector_client()
        feat = smiles_to_vec(molecular_name)
        result = knn_search(index_client, index_name, feat, top_k)
        res_smi = []
        for k,v in result:
            smile = get_attr(index_client, index_name, k, 'smiles')
            res_smi.append(smile[0])
        return res_smi

    except Exception as e:
        logging.error(e)
        return "Fail with error {}".format(e)
