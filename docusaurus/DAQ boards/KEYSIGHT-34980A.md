
# KEYSIGHT 34980A

## Instrument Card

The Keysight 34980A Multifunction Switch/Measure unit is designed for R&D and
manufacturing test engineers who are working in design verification, automated
test or data acquisition and are either looking to upgrade their existing systems or
are in need of a new, cost-effective alternative

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 34980A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 34980A DAQ board using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_34980A import Keysight34980A

# Create an instance of the instrument
daq = Keysight34980A('daq', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
daq.connect()

# Perform operations on the instrument
daq.reset()
daq.disconnect_all()

# Disconnect from the instrument
daq.disconnect()
```

This script creates an instance of the `Keysight34980A` instrument with the name 'daq' and the specified address ('TCPIP0::192.168.1.1::INSTR'). It then connects to the instrument using the `connect()` method.

After connecting, you can perform various operations on the instrument, such as resetting it (`reset()`) and disconnecting all connections (`disconnect_all()`).

Finally, you can disconnect from the instrument using the `disconnect()` method.

