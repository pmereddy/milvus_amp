import subprocess
import os

auth=os.environ.get('MILVUS_AUTH', 'false').lower()
if auth!='false' and auth!='true':
    auth='false'

command = ["/usr/bin/nohup", "$HOME/.local/bin/milvus-server", "--data $HOME/milvus-data", "--authorization-enabled", auth, " & "]

process = subprocess.Popen(command, 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=False)

print(process.pid)
