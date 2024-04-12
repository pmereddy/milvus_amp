#!/bin/bash

rm -rf $HOME/milvus-data
nohup $HOME/.local/bin/milvus-server --debug --data $HOME/milvus-data --authorization-enabled true >/dev/null 2>&1 &
 
pid="$!"
disown -a $pid
exit 0
