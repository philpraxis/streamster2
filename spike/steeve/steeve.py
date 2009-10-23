#!/usr/bin/python
# -*- coding: utf-8 -*-

from entangled.kademlia.node import *
from entangled.kademlia.datastore import *
from entangled.kademlia.routingtable import *
from entangled.kademlia.contact import *
from entangled.kademlia.protocol import *
import time


# INFOS SUR LES CLASSES

# contact -> noeud distant
# node -> noeud local
# datastore -> stockage des infos (STORE)
# protocol -> implémentations bas-niveau des fonctions réseaux du protocole Kademlia
# routingtable -> table de routage




def main():
    myId = 'steeve1234'
    #création du datastore pour stocker les infos à partager
    myDataStore = DictDataStore()
    myDataStore.setItem('key1', 'value1', time.time(), None, myId)
    myDataStore.setItem('key2', 'value2', time.time(), None, myId)
    print str(myDataStore.keys())
    print myDataStore.__getitem__('key1')
    myDataStore.__delitem__('key2')
    print str(myDataStore.keys())

    #création de ma table de routage
    myTreeRoutingTable = TreeRoutingTable(myId)

    # mon noeud
    myNode = Node(8600, myDataStore, myTreeRoutingTable, None)
    myNode.printContacts()

    # protocole
    myProto = KademliaProtocol(myNode)

    # mon premier contact
    myFirstContact = Contact('contact111', '192.168.1.11', 1111, myProto)

    # ajout d'un contact
    myTreeRoutingTable.addContact(myFirstContact)
    print str(myTreeRoutingTable.getContact('contact111'))
    myNode.printContacts()
    

main()

