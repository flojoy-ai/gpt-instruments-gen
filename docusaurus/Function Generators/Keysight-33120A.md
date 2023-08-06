
# Keysight 33120A

## Instrument Card

33120A Function / Arbitrary Waveform Generator, 15 MHz

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the Keysight 33120A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments import HP33120A

# Create a VISA adapter for communication
adapter = VISAAdapter("GPIB0::10::INSTR")

# Connect to the Keysight 33120A Function Generator
generator = HP33120A(adapter)

# Set the waveform shape to sinusoid
generator.shape = 'sinusoid'

# Set the frequency to 1 kHz
generator.frequency = 1000

# Set the amplitude to 1 Vpp
generator.amplitude = 1

# Enable the output
generator.output = True

# Generate a system beep
generator.beep()

# Disconnect from the instrument
generator.disconnect()
```

This script first creates a VISA adapter using the `VISAAdapter` class from Pymeasure. The adapter is initialized with the VISA address of the instrument, which in this case is "GPIB0::10::INSTR".

Then, an instance of the `HP33120A` class is created, passing the adapter as an argument. This represents the Keysight 33120A Function Generator.

The script then sets the waveform shape to sinusoid, frequency to 1 kHz, and amplitude to 1 Vpp using the properties provided by the `HP33120A` class.

Next, the output of the function generator is enabled by setting the `output` property to `True`.

A system beep is generated using the `beep()` method of the function generator.

Finally, the script disconnects from the instrument using the `disconnect()` method.

Note: Make sure to install the necessary dependencies (`pymeasure` and `pyvisa`) before running the script.

