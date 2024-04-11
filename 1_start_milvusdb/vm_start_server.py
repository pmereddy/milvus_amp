import subprocess
import os

auth=os.environ.get('MILVUS_AUTH', 'false').lower()
if auth!='false' and auth!='true':
    auth='false'

subprocess.run(["/usr/bin/nohup $HOME/.local/bin/milvus-servermilvus-server --data $HOME/milvus-data --authorization-enabled & " + str(auth)], shell=False)
