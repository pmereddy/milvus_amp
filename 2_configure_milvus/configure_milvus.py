import subprocess
import os

from milvus import default_server
from pymilvus import connections, utility, milvus_client
import time

auth=os.environ.get('MILVUS_AUTH', 'false').lower()
if auth!='false' and auth!='true':
    auth='false'

with open('/home/cdsw/server.ip', 'r') as f:
    host = f.readline().strip()

if auth == 'true':
    # connect with default creds
    client = milvus_client.MilvusClient(host=host, port=default_server.listen_port, user='root',password='Milvus')
  
    # Create user provided by the user 
    default_na='_not_given_'
    user = os.environ.get('MILVUS_USER', default_na)
    password = os.environ.get('MILVUS_PASSWORD', default_na)
    if user != default_na and password == default_na:
        client.create_user(user,password)
        client.grant_role(user, 'admin')
