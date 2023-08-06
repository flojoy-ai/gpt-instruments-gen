
# KEYSIGHT E8267D

## Instrument Card

E8267D PSG Vector Signal Generator, 100 kHz to 44 GHz

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT E8267D in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT E8267D RF Signal Generator using Qcodes, you can use the following Python script:

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_E8267D import Keysight_E8267D

# Create an instance of the instrument
signal_generator = Keysight_E8267D("signal_generator", "TCPIP0::192.168.1.1::inst0::INSTR")

# Connect to the instrument
signal_generator.connect()

# Print the instrument ID
print("Instrument ID:", signal_generator.IDN())

# Set the frequency to 1 GHz
signal_generator.frequency(1e9)

# Set the power to -10 dBm
signal_generator.power(-10)

# Enable the output
signal_generator.output_enabled(True)

# Disable the output after 1 second
qc.sleep(1)
signal_generator.output_enabled(False)

# Disconnect from the instrument
signal_generator.disconnect()
```

This script imports the necessary modules and creates an instance of the `Keysight_E8267D` instrument class from the Qcodes Keysight driver. It then connects to the instrument using the specified address (replace `"TCPIP0::192.168.1.1::inst0::INSTR"` with the actual address of your instrument).

The script demonstrates some basic operations with the signal generator, such as setting the frequency and power, enabling and disabling the output, and printing the instrument ID. Finally, it disconnects from the instrument.

Note: Make sure you have the Qcodes and Keysight drivers installed before running this script.

