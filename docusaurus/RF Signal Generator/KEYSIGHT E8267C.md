
# KEYSIGHT E8267C

## Instrument Card

E8267C PSG Vector Signal Generator, up to 20 GHz

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT E8267C in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here's a Python script that uses Qcodes to connect to a KEYSIGHT E8267C RF Signal Generator:

```python
from qcodes.instrument.visa import VisaInstrument

# Create an instance of the AgilentE8267C instrument
signal_generator = AgilentE8267C("signal_generator", "TCPIP0::192.168.1.1::INSTR")

# Connect to the instrument
signal_generator.connect()

# Set the frequency to 1 GHz
signal_generator.frequency(1e9)

# Set the power to -10 dBm
signal_generator.power(-10)

# Enable the RF output
signal_generator.output_rf("ON")

# Disconnect from the instrument
signal_generator.disconnect()
```

This script creates an instance of the `AgilentE8267C` instrument with the name "signal_generator" and the specified address. It then connects to the instrument using the `connect()` method.

After connecting, it sets the frequency to 1 GHz using the `frequency()` parameter, sets the power to -10 dBm using the `power()` parameter, and enables the RF output using the `output_rf()` parameter.

Finally, it disconnects from the instrument using the `disconnect()` method.

