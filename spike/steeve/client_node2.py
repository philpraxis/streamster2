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
    myNode = Node(8602, None, None, None)
    a = [('127.0.0.1', 8600)]
    myNode.joinNetwork(a)

    #myNode.iterativeStore('datakey2', 'datavalue2')
    #print "recherche de datas : "

    #print myNode.iterativeFindValue('datakey1').addCallback(printData)
    #print myNode.iterativeFindValue('datakey2').addCallback(printData)
    #print myNode.iterativeFindValue('datakey3').addCallback(printData)
    #myNode.printContacts()

    twisted.internet.reactor.run()


main()