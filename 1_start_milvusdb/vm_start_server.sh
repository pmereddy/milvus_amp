#!/bin/bash

daemonize() {
  pid=$(/bin/bash -c "setsid nohup sh -c '$@' >/dev/null 2>&1 & echo \$!")
  
  # Check for successful fork
  if [[ -n "$pid" ]]; then
    disown -a >/dev/null 2>&1
  else
    echo "Failed to daemonize!"
  fi

  exit 0
}

daemonize "$@"
