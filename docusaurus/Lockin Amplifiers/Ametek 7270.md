
# Ametek 7270

## Instrument Card

The model 7270 sets a new standard for general-purpose DSP lock-in amplifiers.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Since 1930, our talented and diverse workforce has been delivering **differentiated technology solutions** to create strong, sustainable and profitable growth. <a href=https://www.ametek.com/>Website</a>.

<ul>
  <li>Headquarters: US</li>
  <li>Yearly Revenue (millions, USD): 6200.0</li>
</ul>
</details>

## Connect to the Ametek 7270 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments.ametek import Ametek7270

# Create a VISA adapter for communication
adapter = VISAAdapter("GPIB0::1::INSTR")

# Connect to the Ametek 7270 Lockin Amplifier
lockin = Ametek7270(adapter)

# Set the reference mode to Single
lockin.set_reference_mode(0)

# Set the instrument to voltage control mode
lockin.set_voltage_mode()

# Set the sensitivity to 100 nV
lockin.sensitivity = 100e-9

# Read the X value
x_value = lockin.x
print("X value:", x_value)

# Read the Y value
y_value = lockin.y
print("Y value:", y_value)

# Set the instrument to current control mode with low noise
lockin.set_current_mode(low_noise=True)

# Set the sensitivity to 1 µV
lockin.sensitivity = 1e-6

# Read the magnitude
magnitude = lockin.mag
print("Magnitude:", magnitude)

# Shutdown the instrument
lockin.shutdown()
```

This script demonstrates how to connect to the Ametek 7270 Lockin Amplifier using a VISA adapter, set the reference mode, control the instrument mode, set the sensitivity, and read measurements from the lock-in amplifier. Finally, it shuts down the instrument.

Note: Make sure to install the required dependencies (`pymeasure`, `pyvisa`, and `pyvisa-py`) before running the script.

