
# KEYSIGHT 33511B

## Instrument Card

The 33511B waveform generator provides Keysight's exclusive Trueform technology which offers unmatched capabilities for generating a full range of signals for your most demanding measurements.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 33511B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 33511B RF Signal Generator using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_33XXX import WaveformGenerator_33XXX

# Create an instance of the instrument
signal_generator = WaveformGenerator_33XXX('signal_generator', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
signal_generator.connect_message()

# Now you can use the instrument to control the signal generator
# For example, you can set the frequency of channel 1 to 1 MHz
signal_generator.ch1.frequency(1e6)

# You can also read the current frequency setting
frequency = signal_generator.ch1.frequency()
print(f"The current frequency is: {frequency} Hz")

# Don't forget to close the connection when you're done
signal_generator.close()
```

Note: Replace `'TCPIP0::192.168.1.1::INSTR'` with the actual VISA resource name of your KEYSIGHT 33511B RF Signal Generator.

