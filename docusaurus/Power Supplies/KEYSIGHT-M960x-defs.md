
# KEYSIGHT M960x defs

## Instrument Card

PXI source/measure units are the source and measurement resources of voltage and current for test applications requiring high accuracy, high resolution, and measurement flexibility

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT M960x defs in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes


```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_M960x import Keysight_M960x

# Connect to the power meter
power_meter = Keysight_M960x("power_meter", "TCPIP0::192.168.1.1::inst0::INSTR")

# Print the power meter identification
print("Power Meter Identification:")
print("Vendor:", power_meter.vendor())
print("Model:", power_meter.model())
print("Serial Number:", power_meter.serial_number())

# Set the power meter to measure power
power_meter.measurement_function("POWER")

# Read the power measurement
power = power_meter.measure()

# Print the power measurement
print("Power Measurement:", power)

# Disconnect from the power meter
power_meter.close()
```

This script connects to the power meter using the IP address "192.168.1.1" and the instrument name "inst0". It then retrieves the power meter identification information, sets the measurement function to "POWER", and reads the power measurement. Finally, it closes the connection to the power meter.

Note: Make sure to replace the IP address and instrument name with the correct values for your setup.

