
# KEYSIGHT - 34450A

## Instrument Card

Turbo charge your production line with the Keysight 34450A 5.5-digit multimeter with OLED display. With its fast speed of up to 190 readings per second, you can increase your manufacturing throughput tremendously.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT - 34450A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments import Agilent34450A

# Create a VISA adapter for the instrument
adapter = VISAAdapter("USB0::0x0957::0x0607::MY44012345::INSTR")

# Create an instance of the Agilent34450A instrument
dmm = Agilent34450A(adapter)

# Reset the instrument
dmm.reset()

# Configure the instrument to measure voltage
dmm.configure_voltage()

# Read the voltage measurement
voltage = dmm.voltage
print("Voltage:", voltage)

# Configure the instrument to measure current
dmm.configure_current()

# Read the current measurement
current = dmm.current
print("Current:", current)

# Shutdown the instrument
dmm.shutdown()
```

In this example, we first create a VISA adapter using the appropriate address for your instrument. Then, we create an instance of the Agilent34450A instrument using the adapter. We can then use the instrument's methods to perform various operations, such as resetting the instrument, configuring the measurement mode, and reading measurements. Finally, we shutdown the instrument to release any resources.

Note: Make sure to replace `"USB0::0x0957::0x0607::MY44012345::INSTR"` with the actual address of your instrument.

