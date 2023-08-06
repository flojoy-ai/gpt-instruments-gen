
# KEYSIGHT 34934A

## Instrument Card

The Keysight 34934A module for the 34980A Multifunction Switch/Measure Unit offers the highest density matrix for connecting paths between your device under test and your test equipment, allowing for multiple instrument connections to multiple points on your device under test at the same time.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 34934A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 34934A DAQ board using Qcodes, you can use the following Python script:

```python
from qcodes import VisaInstrument

# Connect to the KEYSIGHT 34934A DAQ board
daq_board = VisaInstrument('DAQ_board', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Print the relay protection mode
print(daq_board.protection_mode())

# Set the relay protection mode to 'AUTO100'
daq_board.protection_mode('AUTO100')

# Convert (row, column) pairs to channel numbers
channel_list = daq_board.to_channel_list([(1, 2), (3, 4)], 'MH')
print(channel_list)

# Disconnect from the DAQ board
daq_board.close()
```

Note: Replace `'TCPIP0::192.168.1.1::inst0::INSTR'` with the actual VISA address of your KEYSIGHT 34934A DAQ board.

This script connects to the KEYSIGHT 34934A DAQ board using the VISA address `'TCPIP0::192.168.1.1::inst0::INSTR'`. It then retrieves and prints the current relay protection mode using `daq_board.protection_mode()`. The relay protection mode is set to `'AUTO100'` using `daq_board.protection_mode('AUTO100')`. The `to_channel_list` method is used to convert the `(row, column)` pairs `[(1, 2), (3, 4)]` to channel numbers. Finally, the script closes the connection to the DAQ board using `daq_board.close()`.

