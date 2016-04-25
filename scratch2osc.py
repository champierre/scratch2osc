#!/usr/bin/env python

import sys
import os
import scratch
import time
from OSC import OSCClient, OSCMessage

VERSION = "0.0.1"
OSC_HOST = "127.0.0.1"
OSC_PORT = 8000
OSC_ADDR = '/scratch/test'

def connect():
    try:
        return scratch.Scratch()
    except scratch.ScratchError:
        print _("Error: Unable to connect to Scratch. Scratch may be not running or the remote sensor connections may be not enabled.")
        return None

def _listen(s):
    while True:
        try:
            yield s.receive()
        except scratch.ScratchError:
            print _("Error: Disconnected from Scratch.")
            raise StopIteration

def listen(s, osc_client):
    for msg in _listen(s):
        if (msg):
            print "Received: %s" % str(msg)
            if msg[0] == 'broadcast':
                if msg[1] == 'goo':
                    osc_client.send(OSCMessage(OSC_ADDR, 'goo'))
                    print "Send goo to OSC."
                if msg[1] == 'choki'
                    osc_client.send(OSCMessage(OSC_ADDR, 'choki'))
                    print "Send choki to OSC."
                elif msg[1] == 'par':
                    osc_client.send(OSCMessage(OSC_ADDR, 'par'))
                    print "Send par to OSC."
            elif msg[0] == 'sensor-update':
                print "sensor-update"

def main():
  print "================="
  print "Sratch2OSC %s" % VERSION
  print "================="
  print ""

  while True:
    s = connect()

    osc_client = OSCClient()
    osc_client.connect(OSC_HOST, OSC_PORT)

    if (s):
      print _("Connected to Scratch")

      s.broadcast("goo")
      s.broadcast("choki")
      s.broadcast("par")

      listen(s, osc_client)
    time.sleep(5)

main()
