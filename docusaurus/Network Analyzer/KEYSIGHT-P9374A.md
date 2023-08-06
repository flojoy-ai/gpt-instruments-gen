
# KEYSIGHT P9374A

## Instrument Card

P9374A Keysight Streamline USB Vector Network Analyzer, 20 GHz. Compact, faceless, USB vector network analyzer (VNA). Affordable full two-port VNA which dramatically reduces your size of test. Up to 20 GHz.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT P9374A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_P9374A import KeysightP9374A

# Create an instance of the KeysightP9374A instrument
pna = KeysightP9374A('pna', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Connect to the instrument
pna.connect()

# Perform operations with the instrument
pna.get_options()

# Disconnect from the instrument
pna.disconnect()
```

Explanation:
1. Import the necessary modules: `qcodes` and the `KeysightP9374A` instrument driver.
2. Create an instance of the `KeysightP9374A` instrument with a name ('pna') and the instrument's address ('TCPIP0::192.168.1.1::inst0::INSTR').
3. Connect to the instrument using the `connect()` method.
4. Perform any desired operations with the instrument, such as calling the `get_options()` method.
5. Disconnect from the instrument using the `disconnect()` method.

