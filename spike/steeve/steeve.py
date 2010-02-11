#!/usr/bin/python
# -*- coding: utf-8 -*-

from entangled.kademlia.node import *
from entangled.kademlia.datastore import *
from entangled.kademlia.routingtable import *
from entangled.kademlia.contact import *
from entangled.kademlia.protocol import *
import time, hashlib


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
    # on lui attribue des éléments
    myDataStore.setItem('key1', 'value1', time.time(), None, myId)
    myDataStore.setItem('key2', 'value2', time.time(), None, myId)
    myDataStore.setItem('key3', 'value3', time.time(), None, myId)
    myDataStore.setItem('key4', 'value4', time.time(), None, myId)

    print str(myDataStore.keys())			# affichage des clés du datastore
    print myDataStore.__getitem__('key1')	# affichage de la valeur de la clé demandée

    myDataStore.__delitem__('key2')			# suppression de l'élément
    myDataStore.setItem('key5', 'value5', time.time(), None, myId)	# ajout d'une élément
    print str(myDataStore.keys())			# affichage des clés du datastore


    #création de ma table de routage
    myTreeRoutingTable = TreeRoutingTable(myId)

    # mon noeud
    myNode = Node(8600, myDataStore, None, None)

    # protocole
    myProto = KademliaProtocol(myNode)

    # mon premier contact
    myFirstContact = Contact('contact111', '192.168.1.1', 1111, myProto)    
    # mon second contact
    mySecondContact = Contact('contact222', '192.168.1.12', 1111, myProto)
    # mon troisieme contact
    myThirdContact = Contact('contact333', '192.168.1.13', 1111, myProto)    


    # manipulation des contacts au niveau du noeud "myNode"
    print "\n\n\tPremier Noeud \n - ajout de 2 contacts"
    myNode.addContact(myFirstContact)
    myNode.addContact(mySecondContact)
    print " - affichage des contacts du noeud"
    myNode.printContacts()					# affichage de tous les contacts du noeud
    print " - suppression du contact : contact111"
    myNode.removeContact('contact111')                           # remove inefficace 
    print " - affichage des contacts du noeud"
    myNode.printContacts()		# on peut voir que la suppression du contact : contact111 n'a pas fonctionné
    
    print " - recherche du contact : contact111"
    print myNode.findContact('contact111')					# retourne un Deferred cf Twisted, pk ???
    print " - recherche du noeud : contact222"			### ????? QU'EST CE QU'IL RETOURNE ??????????????????????  
    print myNode.findNode('contact222')
    print " - stockage de datas"
    myNode.store('datakey1', 'datavalue1', myId)
    h = hashlib.sha1()
    h.update('datakey1111')
    mkey=h.digest()
    #myNode.iterativeStore(mkey, 'datavalue1111')
    myNode.store('datakey2', 'datavalue2', myId)
    myNode.store('datakey3', 'datavalue3', myId)
    print "recherche de datas : datakey1"
    print myNode.findValue('datakey1')				#recherche de datas



    print "\n\n\n\n Manipulation de la table de routage créée manuellement"
    # ajout de 2 contacts dans notre table de routage créée manuellement
    myTreeRoutingTable.addContact(myFirstContact)
    myTreeRoutingTable.addContact(mySecondContact)
    myTreeRoutingTable.addContact(myThirdContact)
    print "contact111 :"
    print str(myTreeRoutingTable.getContact('contact111'))	# affichage des informations concernant le contact : contact111
    myTreeRoutingTable.removeContact('contact111')
    print "contact222 :"
    print str(myTreeRoutingTable.getContact('contact222'))
    print "les 3 noeuds les plus proches de contact111 :"
    print str(myTreeRoutingTable.findCloseNodes('contact111', 3)) # retourne les noeuds les plus proches sous forme d'une liste


    """print "\n\n\nSecond node\n##################"
    # un second noeud avec lequel on va essayer de communiquer
    yourNode = Node(7885, myDataStore, None, None)
	# son premier contact
    yourFirstContact = Contact('contact888', '192.168.1.85', 1234, myProto)
    yourNode.addContact(yourFirstContact)
    # son second contact
    yourSecondContact = Contact('contact555', '192.168.1.78', 4321, myProto)
    yourNode.addContact(yourSecondContact)
    yourNode.printContacts()"""

    a = [('127.0.0.1', 6666)]	# port source : 8600
    myNode.joinNetwork(a)			# pour se connecter au noeud 127.0.0.1 port UDP 6666
    twisted.internet.reactor.run()
    
    # exemple quand on utilise un table de routage existante (erreur car dans __init__ il n'initialise pas cette table, il le fait seulement lorsque qu'on laisse None comme RootingTable)
    #myNode2 = Node(8602, myDataStore, myTreeRoutingTable, None)
    #myNode2.printContacts()




# probleme avec khashmir : pleins de modifs a faire, car ça a été codé avec une vieille version de python, et pb avec twisted : il faut importer "app" de "twisted.internet" mais il ne doit plus exister




main()

