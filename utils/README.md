# Utilities

You will need Python's [cantools](https://github.com/cantools/cantools) installed to run these utilities.  To install use `python3 -m pip install cantools`.

## dbc_msg_list.py

`dbc_msg_list.py` takes a DBC file name as it's sole argument and lists all the message type defined in that file.  The are unsorted is it can be useful to pipe the output through `sort`.

## dbc_summary.py

`dbc_summary.py` takes a DBC file name as it's sole argument and lists all the message type defined in that file.  For each message type it lists the name if the signal(s) it decodes.
