
# KEYSIGHT E8267D PSG

## Instrument Card

The E8267D PSG Vector Signal Generator is the highest performance, fully-integrated microwave vector signal generator from 100 kHz to 44 GHz, allowing you to create realistic wideband radar, electronic warfare (EW), and satellite communications (SATCOM) waveforms.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT E8267D PSG in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a KEYSIGHT E8267D PSG RF Signal Generator using Qcodes Community, you can use the following Python script:

```python
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument_drivers.Keysight.Keysight_E8267D import Keysight_E8267D

# Connect to the instrument
instrument = Keysight_E8267D("instrument_name", "TCPIP0::192.168.1.1::inst0::INSTR")

# Set the frequency to 1 GHz
instrument.frequency(1e9)

# Set the power to -10 dBm
instrument.power(-10)

# Enable the RF output
instrument.output_rf("ON")

# Disconnect from the instrument
instrument.close()
```

Make sure to replace `"instrument_name"` with the desired name for your instrument and `"TCPIP0::192.168.1.1::inst0::INSTR"` with the actual address of your KEYSIGHT E8267D PSG RF Signal Generator.

The script first imports the necessary modules and classes from Qcodes. Then, it creates an instance of the `Keysight_E8267D` class, passing the instrument name and address as arguments. You can use the `VisaInstrument` class if you don't have a specific driver for your instrument.

After connecting to the instrument, you can use the provided parameters and functions to control it. In the example, the frequency is set to 1 GHz, the power is set to -10 dBm, and the RF output is enabled. Finally, the `close()` method is called to disconnect from the instrument.

Note: This code assumes that you have installed the necessary dependencies and have the correct drivers for the KEYSIGHT E8267D PSG RF Signal Generator.

