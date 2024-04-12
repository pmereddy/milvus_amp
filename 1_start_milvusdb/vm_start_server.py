#import subprocess
 
#subprocess.run(["1_start_milvusdb/vm_start_server.sh"], shell=False)
! /home/cdsw/.local/bin/milvus-server --debug --data $HOME/milvus-data --authorization-enabled true > /dev/null 2>&1 &
