import subprocess
import os

auth=os.environ.get('MILVUS_AUTH', 'false').lower()
if auth!='false' and auth!='true':
    auth='false'

#command = ["/usr/bin/nohup", "$HOME/.local/bin/milvus-server", "--data $HOME/milvus-data", "--authorization-enabled", auth, " & "]
command=f"/usr/bin/nohup $HOME/.local/bin/milvus-server --data $HOME/milvus-data --authorization-enabled {auth} & "

rc=os.system(command)
print(rc)
