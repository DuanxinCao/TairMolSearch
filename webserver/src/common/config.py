import os

TAIR_VECTOR_HOST = os.getenv("TAIR_VECTOR_HOST", "127.0.0.1")
TAIR_VECTOR_PORT = os.getenv("TAIR_VECTOR_PORT", 6379)
TAIR_PASSWOED = os.getenv("TAIR_VECTOR_PORT","default")

VECTOR_DIMENSION = os.getenv("VECTOR_DIMENSION", 64)
NUM = os.getenv("TOPK_NUM", 10)
DEFULT_INDEX = os.getenv("DEFULT_INDEX", "molsearch")


PG_HOST = os.getenv("PG_HOST", "192.168.1.85")
PG_PORT = os.getenv("PG_PORT", 5432)
PG_USER = os.getenv("PG_USER", "postgres")
PG_PASSWORD = os.getenv("PG_PASSWORD", "postgres")
PG_DATABASE = os.getenv("PG_DATABASE", "postgres")
PG_TABLE = os.getenv("PG_TABLE", "molsearch")
