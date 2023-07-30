
# KEYSIGHT 34461A Submodules

## Instrument Card

The 34411A offers Temperature and Capacitance capabilities, in addition to those measurements you have come to expect, such as DCV, ACV, DCI, ACI, 2-wire and 4-wire Resistance, Frequency, Period, Continuity and Diode Test.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 34461A Submodules in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_344xxA import Keysight34461A

# Create an instance of the Keysight34461A driver
dmm = Keysight34461A('dmm', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
dmm.connect()

# Perform measurements or other operations with the instrument

# Disconnect from the instrument
dmm.disconnect()
```

This code imports the necessary modules and creates an instance of the `Keysight34461A` driver, which represents the Keysight 34461A Multimeter. The `name` parameter is set to `'dmm'` and the `address` parameter is set to the IP address of the instrument. The `connect()` method is then called to establish a connection to the instrument, and the `disconnect()` method is called to disconnect from the instrument when finished.

