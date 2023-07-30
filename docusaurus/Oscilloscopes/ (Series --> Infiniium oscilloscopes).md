
#  (Series --> Infiniium oscilloscopes)

## Instrument Card

Infiniium series oscilloscopes feature application-specific software that allows you to gain valuable insight into your design. Whether you are solving tough jitter or noise problems, removing loss due to cables or probes, or simply looking at protocol, this series has the software tools to help you realize your best design.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the  (Series --> Infiniium oscilloscopes) in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a Keysight Infiniium oscilloscope using Qcodes, you can use the following code:

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_6000 import Keysight_6000

# Create an instance of the Keysight_6000 driver
scope = Keysight_6000("scope", "TCPIP0::192.168.1.1::INSTR")

# Connect to the oscilloscope
scope.connect()

# Print the IDN of the oscilloscope
print(scope.IDN())

# Perform other operations with the oscilloscope

# Disconnect from the oscilloscope
scope.disconnect()
```

Make sure to replace `"TCPIP0::192.168.1.1::INSTR"` with the actual VISA address of your oscilloscope.

