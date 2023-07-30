
# KEYSIGHT 34470A Submodules

## Instrument Card

The 34411A offers Temperature and Capacitance capabilities, in addition to those measurements you have come to expect, such as DCV, ACV, DCI, ACI, 2-wire and 4-wire Resistance, Frequency, Period, Continuity and Diode Test.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 34470A Submodules in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_344xxA import Keysight_344xxA

# Create an instance of the Keysight_344xxA driver
dmm = Keysight_344xxA('dmm', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
dmm.connect()

# Perform measurements or other operations with the instrument
# ...

# Disconnect from the instrument
dmm.disconnect()
```

This code imports the necessary modules and creates an instance of the `Keysight_344xxA` driver, which is a subclass of the `Keysight34470A` driver. It then connects to the instrument using the specified address (in this case, a TCP/IP address). After performing any desired measurements or operations, it disconnects from the instrument.

