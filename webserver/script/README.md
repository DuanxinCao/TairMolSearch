# README

## insert_data.py说明

### 参数说明
| 参数             | 描述                         | 默认设置     |
| ---------------- | --------------------------- | ------------ |
| SERVER_ADDR      | tair vector  的 IP 地址      | 127.0.0.1 |
| SERVER_PORT      | tair vector  端口号          | 6379        |
| VECTOR_DIMENSION | 向量维度                     | 64         |
| table_names      | 在tair vector中表名          | [...]        |


### 使用说明

```bash
$ python insert_data.py -f '<file_path>'
# 执行此命令讲文件中的smiles转为fingerprint并导入tair vector
# tair vector 不仅存储向量数据，smiles原分子式也可以作为属性存储进来

[root@494b13ae35e9 script]# python3.7 insert_data.py -f GDB4c.smi
before feature_extract file_path GDB4c.smi
-----len of vectors: 10000
index None <class 'NoneType'>
load idx 1000
load idx 2000
load idx 3000
load idx 4000
load idx 5000
load idx 6000
load idx 7000
load idx 8000
load idx 9000
load idx 10000
```


## thread_gen_smiles_fp.py说明

### 参数说明

| 参数        | 描述                                       | 默认设置                 |
| ----------- | ------------------------------------------ | ------------------------ |
| file_length | 每个文件保存 fingerprint 的数量            | 200000                   |
| vec_dim     | 生成 fingerprint 的维度/位数               | 2048                     |
| FILE_PATH   | 保存.smi文件的目录                         | /data/workspace/test     |
| OUT         | 生成结果的目录                             | /data/workspace/out_test |
| OUT_SMILES  | 转 fingerprint 成功的 smiles 文件路径      | out_smiles               |
| OUT_IDS     | 与 smiles 对应的 ID 文件路径               | out_ids                  |
| OUT_NPY     | 与 smiles 对应 fingerprint 的 npy 文件路径 | out_npy                  |

### 使用说明

```bash
$ python thread_gen_smiles_fp.py
# 执行此命令使用多线程将 FILE_PATH 下的 smiles 转化为 RDKit fingerprint，程序将建立 OUT 等目录存储结果。
```

### 测试数据集
- 来源 https://gdb.unibe.ch/downloads/
- 格式 smiles
- 下载链接: https://zenodo.org/record/5172018/files/GDB4c.smi.gz?download=1