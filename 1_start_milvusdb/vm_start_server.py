from milvus import default_server
from pymilvus import connections, Collection, utility
import multiprocessing
import time
import os
 
def start_milvus():
    try:
        default_server.set_base_dir('milvus-data')
        default_server.start()
    except Exception as e:
        default_server.stop()
        raise (e)

def start_milvus2():
    auth=os.environ.get('MILVUS_AUTH', 'false').lower()
    if auth!='false' and auth!='true':
        auth='false'
    command = ["/usr/bin/nohup", "$HOME/.local/bin/milvus-server", "--data $HOME/milvus-data", "--authorization-enabled", auth, " & "]
    #command=f"/usr/bin/nohup $HOME/.local/bin/milvus-server --data $HOME/milvus-data --authorization-enabled {auth} & "
    rc=os.system(command)
    print(rc)

if __name__ == "__main__":
    p = multiprocessing.Process(target=start_milvus2, daemon=True)
    p.start()
    print("Started MilvusDB server")
    time.sleep(5)


