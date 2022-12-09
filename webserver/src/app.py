import os
import os.path as path
import logging
from common.config import DEFULT_INDEX, NUM
from service.search import do_search
from service.count import do_count
from flask_cors import CORS
from flask import Flask, request, send_file, jsonify
from flask_restful import reqparse
from werkzeug.utils import secure_filename
import numpy as np
from numpy import linalg as LA
import time


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

model = None

@app.route('/api/v1/count')
def do_count_api():
    Table = request.args.get('Table')
    logging.info("Table %s" % Table)
    rows = do_count(Table)
    return "{}".format(rows)


@app.route('/api/v1/search')
def do_search_api(Molecular: str=None, Type: str='similarity', Cid: int=0):

    molecular_name = request.args.get('Molecular')
    search_type = request.args.get('Type')
    cid_num = int(request.args.get('Cid', 0))

    top_k = NUM
    
    logging.info("molecular_name %s, search_type %s" % (molecular_name, search_type))
    
    if search_type != 'similarity':
        return "not support", 400

    if cid_num > 0:
        from pubchempy import get_compounds, Compound
        comp = Compound.from_cid(cid_num)
        molecular_name = comp.isomeric_smiles

    if not molecular_name:
        return "no molecular"
    if molecular_name:
        try:
            res_smi = do_search(DEFULT_INDEX, molecular_name, top_k)
        except:
            return "There has no results, please input the correct molecular and ensure the table has data."
        re = {}
        re["Smiles"] = res_smi
        logging.info("re %s" % re)
        return jsonify(re), 200
    return "not found", 400


@app.route('/api/v1/hello')
def do_test():
    return {"test": "hello world"}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
