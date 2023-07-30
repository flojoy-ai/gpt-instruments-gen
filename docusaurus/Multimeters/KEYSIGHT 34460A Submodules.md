
# KEYSIGHT 34460A Submodules

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

## Connect to the KEYSIGHT 34460A Submodules in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 34460A Submodules Multimeter using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_344xxA import Keysight_34411A

# Create an instance of the Keysight_34411A driver
multimeter = Keysight_34411A(name='multimeter', address='your_device_address')

# Connect to the multimeter
multimeter.connect()

# Now you can use the multimeter to perform measurements
# For example, to measure voltage:
voltage = multimeter.volt()

# Print the measured voltage
print(f"Measured voltage: {voltage} V")

# Disconnect from the multimeter
multimeter.disconnect()
```

Make sure to replace `'your_device_address'` with the actual address of your KEYSIGHT 34460A Submodules Multimeter.

