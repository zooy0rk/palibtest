#!/usr/bin/python

import palib

pulse = palib.PulseObj('Test', None, False)

clients = pulse.pulse_client_list()

for client in clients:
    print client

print 'test'
