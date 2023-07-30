
# Rigol DP821

## Instrument Card

The Rigol DP821 is a dual channel, remote sense programmable DC Power Supply. It has excellent performance, including various analysis functions and has USB Host and Device with LXI option. All of this makes it suitable to meet a wide range of testing requirements.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
RIGOL Technologies, Inc. specializes in development and production of test and measuring equipment and is one of the fastest growing Chinese companies in this sphere.
RIGOL’s line of products includes [digital storage oscilloscopes](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=227), [function/arbitrary waveform generators](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=230), [digital multimeters](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=233), PC-based devices compatible with LXI standard etc. <a href=https://www.rigol.com/>Website</a>.
<br><br>
<ul>
  <li>Headquarters: Beijing, China</li>
  <li>Yearly Revenue (millions, USD): 23.0</li>
</ul>
</details>

## Connect to the Rigol DP821 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument_drivers.rigol.DP8xx import RigolDP821

# Connect to the Rigol DP821 Power Supply
dp821 = RigolDP821('dp821', 'TCPIP0::192.168.1.100::INSTR')

# Add the instrument to the QCoDeS station
station = qc.Station()
station.add_component(dp821)

# Print the instrument information
print(dp821)
```

