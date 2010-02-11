#!/usr/bin/python
# -*- coding: utf-8 -*-

from entangled.kademlia.node import *
from entangled.kademlia.datastore import *
from entangled.kademlia.routingtable import *
from entangled.kademlia.contact import *
from entangled.kademlia.protocol import *
import time, hashlib


def main():
    
    myNode = Node(8601, None, None, None)
    a = [('127.0.0.1', 8600)]
    myNode.joinNetwork(a)
    myNode.iterativeStore('datakey1', 'datavalue1')

    twisted.internet.reactor.run()


main()