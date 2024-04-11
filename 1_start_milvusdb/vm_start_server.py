#import subprocess
 
#subprocess.run(["1_start_milvusdb/vm_start_server.sh", "$HOME/.local/bin/milvus-server", "--data", "$HOME/milvus-data", "--authorization-enabled", "true"], shell=False)
! /home/cdsw/.local/bin/milvus-server --data $HOME/milvus-data --authorization-enabled true
