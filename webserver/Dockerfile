FROM conda/miniconda3-centos7

WORKDIR /app
COPY . /app

RUN yum -y update
RUN yum install -y telnet vim libXext libSM libXrender

#RUN cd /app/tair-vector-py && pip install .

RUN conda update -n base -c defaults conda
RUN conda install -c rdkit rdkit -y
RUN pip install -r /app/requirements.txt

RUN mkdir -p /tmp/result-mols

CMD python src/app.py