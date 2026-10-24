#!/usr/bin/python
#
# Display a sumary of what messages and signals are handled in a DBC file
#

import cantools, sys

from pprint import pprint



def print_msg(msg, indent):
  print(f'{indent}0x{msg.frame_id:03x}: {msg.name}')
  for sig in msg.signals:
    print(f'  {sig.name}')
  for submsg in msg.contained_messages:
    print_msg(submsg, indent + '  ')



if len(sys.argv) < 2:
  print('Please supply the file name of the DBC file to create summary of')
  exit(10)
  
db = cantools.database.load_file(sys.argv[1])
for msg in db.messages:
  print_msg(msg, '')

