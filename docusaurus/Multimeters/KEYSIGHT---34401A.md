
# KEYSIGHT - 34401A

## Instrument Card

The Keysight Technologies, Inc. 34401A multimeter gives you the performance you need for fast, accurate bench and system testing. The 34401A provides a combination of resolution, accuracy and speed that rivals DMMs costing many times more. 6½ digits of resolution

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT - 34401A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes


```python
from qcodes.instrument_drivers.Keysight.Keysight_344XXA import Keysight_344XXA

# Create an instance of the Keysight_344XXA driver
multimeter = Keysight_344XXA('multimeter', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the multimeter
multimeter.connect()

# Perform some measurements
voltage = multimeter.volt()
current = multimeter.curr()

# Print the measurement results
print(f"Voltage: {voltage} V")
print(f"Current: {current} A")

# Disconnect from the multimeter
multimeter.disconnect()
```

In this script, we import the `Keysight_344XXA` driver from the `qcodes.instrument_drivers.Keysight` module. We then create an instance of the driver, specifying the name of the instrument (`multimeter`) and the VISA resource name (`TCPIP0::192.168.1.1::INSTR`). 

Next, we connect to the multimeter using the `connect()` method. We can then perform measurements using the various measurement functions provided by the driver, such as `volt()` for voltage measurements and `curr()` for current measurements. 

Finally, we print the measurement results and disconnect from the multimeter using the `disconnect()` method.

Note: Make sure to replace `'TCPIP0::192.168.1.1::INSTR'` with the actual VISA resource name of your KEYSIGHT - 34401A Multimeter.

