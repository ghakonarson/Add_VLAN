#!/usr/bin/python
#
# A simple script to add vlan to Juniper EX swithces
# Usage: python add_vlan.py IP_ADDRESS USERNAME VLAN_NAME VLAN_TAG_NUMBER
#
# 2016 Gunnar Hakonarson
#
import sys
import getpass
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
ip = (sys.argv[1])
user = (sys.argv[2])
vlanname = (sys.argv[3])
vlannumber = (sys.argv[4])
pw = getpass.getpass()
dev = Device(ip, user = user, password = pw)
vlanadd = "set vlans " + vlanname + " vlan-id " + vlannumber
print "Contacting device...."
print ""
dev.open()
cfg = Config(dev)
#Lock config file for commit
cfg.lock()
cfg.load(vlanadd, format="set", merge=True)
#print cfg.diff() <- Printout the configuration to be commited
cfg.commit(comment="Commited using add_vlan script")
#Release config file
cfg.unlock()
