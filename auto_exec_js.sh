#!/bin/bash

################################################################################
# Author: Iradufasha Bikri
# Date: 24/05/2024
# Description: Script to automatically set executable permission for JavaScript,
# Python, and C files when created
#
# SETUP:
#     (1) MAKE SURE that this file is exactly here: ~/exec_auto_asigner.sh and
#           for the last time run "chmod u+x ~/exec_auto_asigner.sh"
#     (2) SET ALIASES(keyword to trigger it while in terminal globally):
#         - special team vi run "vi ~/.bashrc"  and append these line(indentation not needed);
#             alias sexc="nohup ~/exec_auto_asigner.sh &"
#             alias kexc="pkill -f exec_auto_asigner.sh"
#     (3) MAKE YOUR SYSTEM AWARE OF SUCH CHANGES
#         $ source ~/.bashrc
#     (4) INSTALL DEPENDENCY
#         $ sudo apt-get install inotify-tools
# USAGE(in your ternminal type...):
#     - "sexc" to start monitoring for file creation events.(Discraimer "sexc" stands for "start exec_auto_asigner")
#     - "kexc" to kill the listening process
#
#    Now no more endless "chmod u+x *.js" (😀)
#    NB: This is in beta so, judge for your self resorce usage(for me it was using 262.1kb of memory) 
################################################################################

# Function to set executable permission for files
set_exec_permission() {
    chmod +x "$1"
    notify-send "Executable permission set for: $1"
}

# Function to handle cleanup on script termination
cleanup() {
    echo ">>> exec_auto_asigner.sh terminated <<<"
    exit
}

# Trap SIGINT signal (Ctrl+C) to execute cleanup function
trap cleanup SIGINT

# Listen for file creation events for JavaScript, Python, and C files
while true; do
    file=$(inotifywait -q -e create --format '%w%f' .)
    if [[ "$file" == *.js || "$file" == *.py || "$file" == *.c ]]; then
        set_exec_permission "$file" &
    fi
done