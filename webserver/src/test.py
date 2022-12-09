import redis
from indexer.index import tair_vector_client, knn_search
from common.config import DEFULT_INDEX, NUM
from encoder.encode import smiles_to_vec

def do_test():
    client = tair_vector_client()
    index = client.get_index(DEFULT_INDEX)
    print ('index', index, type(index))
    
    smile="CCOC(=O)c1c(NC(=O)CN(C)C)sc2c1CCCCC2"
    feat = smiles_to_vec(smile)
    print ('search smile', smile, 'feat', feat)
    
    result = knn_search(client, DEFULT_INDEX, feat, 10)
    print ('result', result, type(result))
    
    for key,dis in result.items():
        smile = client.hmget(DEFULT_INDEX, key, 'smiles')[0].decode("utf-8")
        print (key, dis, smile)

if __name__ == "__main__":
    do_test()
