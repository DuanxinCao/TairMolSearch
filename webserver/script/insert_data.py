
import getopt
import sys
from rdkit import DataStructs
from rdkit import Chem
import redis
import os
from tair import Tair
from tair.tairvector import DataType,DistanceMetric,Constants,TairVectorIndex

SERVER_ADDR = os.getenv("TAIR_VECTOR_HOST", "127.0.0.1")
SERVER_PORT = os.getenv("TAIR_VECTOR_PORT", 6379)
PASSWORD = os.getenv("TAIR_VECTOR_PASSWORD","default")

VECTOR_DIMENSION = os.getenv("VECTOR_DIMENSION", 64)
NUM = os.getenv("TOPK_NUM", 10)
DEFULT_INDEX = os.getenv("DEFULT_INDEX", "molsearch")


def smiles_to_vec(smiles):
    mols = Chem.MolFromSmiles(smiles)
    # fp = AllChem.GetMorganFingerprintAsBitVect(mols, 2, VECTOR_DIMENSION)
    fp = Chem.RDKFingerprint(mols, fpSize=VECTOR_DIMENSION*8)
    hex_fp = DataStructs.BitVectToFPSText(fp)
    # print(hex_fp)
    vec = bytes.fromhex(hex_fp)
    #print (vec)
    vec_list = list(vec)
    vector = []
    for v in vec_list:
        tmp = [1 if ((1 << (7 - i)) & v) else 0 for i in range(8)]
        vector.extend(tmp)
    return vector


def get_feature_from_file(filepath):
    feats = []
    smiles = []
    ids = []
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.split()
            smiles.append(parts[0])
            ids.append(parts[1])
            vec = line[line.find('['):]
            print (parts[0], parts[1], vec, type(vec))
            feats.append(vec)
    return  feats, smiles, ids


def feature_extract(filepath):
    feats = []
    smiles = []
    ids = []
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.split()
            # print(parts)
            try:
                ids.append(int(parts[1]))
                smiles.append(parts[0])
                vec = smiles_to_vec(parts[0])
                feats.append(vec)
            except :
                print(line)
    return feats, smiles, ids


def do_load(file_path):
    print ("before feature_extract file_path %s" % file_path)
    vectors, names, ids = feature_extract(file_path)
    print("-----len of vectors:",len(vectors))

    client = Tair(SERVER_ADDR, SERVER_PORT,password=PASSWORD)

    if client is not None:
        index = client.tvs_get_index(str(DEFULT_INDEX))
        print ('index', index, type(index))
        if index is None:
            param = {
            'M': 64,
            'ef_construct': 200,
            'max_elements': 20000,
            }
            ret = client.tvs_create_index(DEFULT_INDEX, VECTOR_DIMENSION*8,distance_type=DistanceMetric.Jaccard,data_type=DataType.Binary, **param)
            if not ret:
                print ("create vector index error")
                sys.exit(2)
                
        idx = 0
        while idx<len(vectors) :
            attribute = {'smiles': names[idx]}
            try:
                ret = client.tvs_hset(DEFULT_INDEX, str(ids[idx]), vectors[idx], is_binary=True,**attribute)
            except:
                print ("hset %s error" % idx[idx])
            idx += 1
            if idx % 1000 == 0:
                print ("load idx %s" % idx)

def main(argv):
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "f:h",
            ["help","file="],
        )
        # print(opts)
    except getopt.GetoptError:
        print("Usage:python insert_data.py --file <file_path> ")
        sys.exit(2)

    for opt_name, opt_value in opts:
        if opt_name in ("-f", "--file"):
            file_path = opt_value
            do_load(file_path)
        else:
            print("wrong parameter")
            sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
