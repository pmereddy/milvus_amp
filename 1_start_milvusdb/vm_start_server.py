import subprocess
import time
import sys

#print(subprocess.run(["1_start_milvusdb/vm_start_server.sh"], shell=True))
print(subprocess.run(["nohup $HOME/.local/bin/milvus-server --data $HOME/milvus-data --authorization-enabled true >/dev/null 2>&1 &"], shell=True))
time.sleep(15)

