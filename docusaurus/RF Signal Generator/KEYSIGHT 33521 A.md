
# KEYSIGHT 33521 A

## Instrument Card

Keysight 33500 Series function/arbitrary waveform generators offer the highest signal fidelity and implement a new breakthrough technology that provides you with the ability to generate more accurate arbitrary waveforms. With 10x better jitter than anything in their class, they offer unparalleled control of signal frequency for your most challenging measurements.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 33521 A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments import Agilent33500

# Create a VISA adapter for the instrument
adapter = VISAAdapter("GPIB::1")

# Connect to the KEYSIGHT 33521A RF Signal Generator
generator = Agilent33500(adapter)

# Set the output waveform shape to sine
generator.shape = 'SIN'

# Set the output frequency to 1 kHz
generator.frequency = 1e3

# Set the output amplitude to 1 Vpp
generator.amplitude = 1

# Enable the output
generator.output = True

# Disconnect from the instrument
generator.disconnect()
```

This script first creates a VISA adapter using the `VISAAdapter` class from Pymeasure. The adapter is initialized with the VISA address of the instrument, in this case, "GPIB::1".

Then, an instance of the `Agilent33500` class is created, passing the VISA adapter as the argument. This class represents the KEYSIGHT 33521A RF Signal Generator.

The script then sets the output waveform shape to sine, the output frequency to 1 kHz, and the output amplitude to 1 Vpp. Finally, it enables the output of the signal generator.

Note that you may need to modify the VISA address ("GPIB::1") to match the actual address of your instrument.

Let me know if you have any questions!

