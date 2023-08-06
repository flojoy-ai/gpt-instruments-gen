
# Keisight 8116A

## Instrument Card

8116A 50 MHZ PULSE/FUNCTION GENERATOR

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the Keisight 8116A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments.hp import HP8116A

# Create a VISA adapter for the instrument
adapter = VISAAdapter("GPIB0::9::INSTR")

# Connect to the instrument
instrument = HP8116A(adapter)

# Set the frequency to 1 kHz
instrument.frequency = 1e3

# Set the amplitude to 1 V
instrument.amplitude = 1

# Enable the output
instrument.output_enabled = True

# Disconnect from the instrument
instrument.shutdown()
```

This script connects to the instrument using a VISA adapter, sets the frequency to 1 kHz, sets the amplitude to 1 V, enables the output, and then disconnects from the instrument.

