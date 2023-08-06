
# KEYSIGHT - 34411A

## Instrument Card

The Keysight Technologies, Inc. 34411A multimeter gives you the performance you need for fast, accurate bench and system testing. The 34411A provides a combination of resolution, accuracy and speed that rivals DMMs costing many times more. 6½ digits of resolution

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT - 34411A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT - 34411A Multimeter using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_344XXA import Keysight_344XXA

# Create an instance of the Keysight_344XXA driver
multimeter = Keysight_344XXA('multimeter', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the multimeter
multimeter.connect()

# Perform measurements or set parameters using the multimeter object

# Disconnect from the multimeter
multimeter.disconnect()
```

This script imports the `Keysight_344XXA` driver from the `qcodes.instrument_drivers.Keysight` module. It then creates an instance of the driver, specifying a name for the instrument and the VISA resource address of the multimeter.

The `connect()` method is called to establish a connection to the multimeter. You can then perform measurements or set parameters using the methods and properties provided by the `multimeter` object.

Finally, the `disconnect()` method is called to close the connection to the multimeter.

