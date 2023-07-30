
# KEYSIGHT 34411A Submodules

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

## Connect to the KEYSIGHT 34411A Submodules in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
from qcodes.instrument_drivers.Keysight.Keysight_34411A import Keysight_34411A

# Create an instance of the Keysight_34411A driver
multimeter = Keysight_34411A(name='multimeter', address='COM1')

# Connect to the multimeter
multimeter.connect()

# Perform measurements or other operations with the multimeter

# Disconnect from the multimeter
multimeter.disconnect()
```

In this code, we import the `Keysight_34411A` class from the `qcodes.instrument_drivers.Keysight.Keysight_34411A` module. We then create an instance of the `Keysight_34411A` driver with the name 'multimeter' and the address 'COM1'. We connect to the multimeter using the `connect()` method, perform any desired measurements or operations, and finally disconnect from the multimeter using the `disconnect()` method.

