import subprocess
import os

auth=os.environ.get('MILVUS_AUTH', 'false').lower()
if auth!='false' and auth!='true':
    auth='false'

print(subprocess.run(["milvus-server --data $HOME/milvus-data --authorization-enabled " + str(auth)], shell=True))
