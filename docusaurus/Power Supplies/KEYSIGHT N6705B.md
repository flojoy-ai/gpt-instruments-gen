
# KEYSIGHT N6705B

## Instrument Card

The N6705B is a 4-slot mainframe that accepts up to 4 DC Power Modules, and up to 600 W total DC Power Module output power. The modules are ordered separately. 

N6705B accepts the same modules as N6700 Modular Power System, with over 30 modules to choose from

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N6705B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT N6705B Power Supply using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_67XXB import Keysight_67XXB

# Create an instance of the N6705B instrument
n6705b = Keysight_67XXB('n6705b', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Print the instrument's IDN information
print(n6705b.get_idn())

# Access the channels of the instrument
channel1 = n6705b.ch1
channel2 = n6705b.ch2
channel3 = n6705b.ch3
channel4 = n6705b.ch4

# Set the voltage and current for channel 1
channel1.source_voltage(3.0)
channel1.source_current(0.5)

# Enable channel 1
channel1.enable('on')

# Read the voltage and current from channel 1
voltage = channel1.voltage()
current = channel1.current()

# Print the measured voltage and current
print(f"Voltage: {voltage} V")
print(f"Current: {current} A")

# Disable channel 1
channel1.enable('off')

# Close the connection to the instrument
n6705b.close()
```

This script creates an instance of the `Keysight_67XXB` instrument, connects to the N6705B Power Supply at the specified address, and performs various operations such as setting voltage and current, enabling/disabling channels, and reading measured voltage and current.

Note: Make sure to replace `'TCPIP0::192.168.1.1::inst0::INSTR'` with the actual address of your N6705B Power Supply.

