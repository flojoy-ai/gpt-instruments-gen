
# KEYSIGHT M960(X --> Series)A

## Instrument Card

PXI source/measure units are the source and measurement resources of voltage and current for test applications requiring high accuracy, high resolution, and measurement flexibility

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT M960(X --> Series)A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here is a Python script that uses Qcodes to connect to a KEYSIGHT M960X Power Meter:

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.KeysightM960x import KeysightM960x

# Create an instance of the KeysightM960x instrument
power_meter = KeysightM960x("power_meter", address="TCPIP0::192.168.1.1::inst0::INSTR")

# Connect to the instrument
power_meter.connect()

# Print the instrument IDN information
print(power_meter.get_idn())

# Set the output voltage level to 1V
power_meter.voltage_level(1)

# Enable the output
power_meter.output(True)

# Measure the current
current = power_meter.measure_data()[1]
print(f"Measured current: {current} A")

# Disable the output
power_meter.output(False)

# Disconnect from the instrument
power_meter.disconnect()
```

Note: Replace `"TCPIP0::192.168.1.1::inst0::INSTR"` with the actual address of your KEYSIGHT M960X Power Meter.

