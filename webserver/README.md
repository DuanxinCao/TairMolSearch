# Search molecular

## Api
### /api/v1/search 
#### methods
    POST
#### PARAM

|           |     |                                               |
| --------- | --- | --------------------------------------------- |
| Table     | str | tair vector index name, defult molsearch      |
| Num       | int | top k                                         |
| Molecular | str | COc1ccc(cc1)SCCC(=O)NCCNS(=O)(=O)c1cccc(c1)Cl |

### /api/v1/count
#### methods
	POST
#### PARAM

|       |     |                                          |
| ----- | --- | ---------------------------------------- |
| Table | str | tair vector index name, defult molsearch |

# Env

|                  |                                 |
| ---------------- | ------------------------------- |
| TAIR_VECTOR_HOST | tair vector host                |
| TAIR_VECTOR_PORT | tair vector port                |
| VECTOR_DIMENSION | default vector dimension number |
| DATA_PATH        | mols data path                  |
| SIM_TABLE        | similarity_table                |
| SUB_TABLE        | superstructure_table            |
| SUPER_TABLE      | substructure_table              |



## how to use

### tairv4 vector search
- start tair vector server
  
### webserver && webclient

1. build image
    - docker build --network=host -f Dockerfile -t tair-molserver:1.0.0 .    

2. start webserver container
    - docker run -td -p 35001:5000 -e "TAIR_VECTOR_HOST=30.250.144.44" -e "TAIR_VECTOR_PORT=6379" tair-molserver:1.0.0
    - notice: Make sure the connection to the tair vector server is normal in container

3. [start webclient container]((TairMolSearch/webclient/README.md))

4. visit webclient  http://127.0.0.1:8001/

### insert_data to tair vector

1. step into webserver container
    - docker exec -it `docker ps -a |grep tair-molserver |awk '{print $1}'` bash

2. [import README.md](TairMolSearch/webserver/script/README.md)

3. 测试数据集: https://zenodo.org/record/5172018/files/GDB4c.smi.gz?download=1