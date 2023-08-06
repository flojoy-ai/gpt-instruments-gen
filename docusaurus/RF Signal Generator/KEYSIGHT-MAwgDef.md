
# KEYSIGHT MAwgDef

## Instrument Card



<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT MAwgDef in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT MAwgDef RF Signal Generator using Qcodes, you can use the following code:

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_MAwgDef import Keysight_MAwgDef

# Create an instance of the instrument
mawg = Keysight_MAwgDef("mawg", "TCPIP0::192.168.1.1::INSTR")

# Connect to the instrument
mawg.connect()

# Now you can use the instrument to perform various operations
# For example, you can set the output frequency
mawg.frequency(1e9)

# Disconnect from the instrument
mawg.disconnect()
```

Note that you need to replace `"TCPIP0::192.168.1.1::INSTR"` with the actual VISA address of your KEYSIGHT MAwgDef RF Signal Generator.

