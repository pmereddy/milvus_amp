import subprocess
import time
import sys

print(subprocess.run(["1_start_milvusdb/vm_start_server.sh"], shell=True))
time.sleep(15)
