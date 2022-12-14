import os
import numpy as np
from rdkit import DataStructs
from rdkit import Chem
import math
from rdkit.Chem import AllChem
from common.config import VECTOR_DIMENSION


def smiles_to_vec(smiles):
    mols = Chem.MolFromSmiles(smiles)
    # fp = AllChem.GetMorganFingerprintAsBitVect(mols, 2, VECTOR_DIMENSION)
    fp = Chem.RDKFingerprint(mols, fpSize=VECTOR_DIMENSION*8)
    hex_fp = DataStructs.BitVectToFPSText(fp)
    # print(hex_fp)
    vec = bytes.fromhex(hex_fp)
    # print (vec)
    vec_list = list(vec)
    vector = []
    for v in vec_list:
        tmp = [1 if ((1 << (7 - i)) & v) else 0 for i in range(8)]
        vector.append(tmp)
    return vector
