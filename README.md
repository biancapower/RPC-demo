# Installation

    $ sudo pip3 install rpyc

# Usage

To start a server (slave):

    $ ./run\_server.sh

To start a client interactively:

    $ python3

    >>> import rpyc
    >>> conn = rpyc.classic.connect('localhost')
    >>> conn.execute('print("hello world!")')
    >>> conn.execute('from math import sqrt')
    >>> conn.eval('sqrt(9)')

To deploy the contents of myscript.py:

    $ ./deploy_script.py
