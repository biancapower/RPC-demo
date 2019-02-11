#!/usr/bin/python3
import rpyc
import sys

DEFAULT_HOST = 'localhost'

# pick the host to connect to
if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = DEFAULT_HOST

# connect to the host
conn = rpyc.classic.connect(host)

# now conn is an object allowing actions to be made on the host


# run the script on the host
with open('myscript.py', 'r') as f:
    script = f.read()
    conn.execute(script)
