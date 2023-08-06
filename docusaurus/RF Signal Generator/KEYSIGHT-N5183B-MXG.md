
# KEYSIGHT N5183B MXG

## Instrument Card

N5183B MXG X-Series microwave analog signal generator offers 9 kHz to 40 GHz frequency coverage and near PSG levels of phase noise performance.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N5183B MXG in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
from qcodes.instrument_drivers.Keysight.N51x1 import N51x1
from qcodes.instrument_drivers.Keysight.KeysightN5183B import KeysightN5183B

# Connect to the KEYSIGHT N5183B MXG RF Signal Generator
signal_generator = KeysightN5183B('signal_generator', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Use the signal generator
signal_generator.set_power(10)  # Set the power to 10 dBm
signal_generator.on()  # Turn on the signal generator
signal_generator.output_rf('ON')  # Enable the RF output

# Disconnect from the signal generator
signal_generator.close()
```

Note: Replace `'TCPIP0::192.168.1.1::inst0::INSTR'` with the actual address of your KEYSIGHT N5183B MXG RF Signal Generator.

