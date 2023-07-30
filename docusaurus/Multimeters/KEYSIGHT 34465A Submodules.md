
# KEYSIGHT 34465A Submodules

## Instrument Card

The 34411A offers Temperature and Capacitance capabilities, in addition to those measurements you have come to expect, such as DCV, ACV, DCI, ACI, 2-wire and 4-wire Resistance, Frequency, Period, Continuity and Diode Test.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 34465A Submodules in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 34465A Submodules Multimeter using Qcodes, you can use the following Python script:

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_34465A import Keysight_34465A

# Create an instance of the Keysight_34465A driver
multimeter = Keysight_34465A('multimeter', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the multimeter
multimeter.connect()

# Perform measurements or other operations with the multimeter

# Disconnect from the multimeter
multimeter.disconnect()
```

This script imports the necessary modules and creates an instance of the `Keysight_34465A` driver, specifying a name for the instrument and the address of the multimeter. Then, it connects to the multimeter using the `connect()` method, performs any desired measurements or operations, and finally disconnects from the multimeter using the `disconnect()` method.

