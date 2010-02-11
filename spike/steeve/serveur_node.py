#!/usr/bin/python
# -*- coding: utf-8 -*-

from entangled.kademlia.node import *
from entangled.kademlia.datastore import *
from entangled.kademlia.routingtable import *
from entangled.kademlia.contact import *
from entangled.kademlia.protocol import *
import time, hashlib


def printData(d):
    print d

def main():
    myNode = Node(8600, None, None, None)
    myNode.joinNetwork(None)
    myNode.iterativeStore('datakey3', 'datavalue3')

    twisted.internet.reactor.run()


main()