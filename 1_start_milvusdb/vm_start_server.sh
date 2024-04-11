#!/bin/bash

rm -rf $HOME/milvus-data
$HOME/.local/bin/milvus-server --data $HOME/milvus-data --authorization-enabled true &
pid="$!"
disown -a $pid
exit 0
