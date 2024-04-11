#!/bin/bash

#auth=os.environ.get('MILVUS_AUTH', 'false').lower()
#if auth!='false' and auth!='true':
#    auth='false'

/usr/bin/nohup $HOME/.local/bin/milvus-server --data $HOME/milvus-data --authorization-enabled true &
echo "start completed"
