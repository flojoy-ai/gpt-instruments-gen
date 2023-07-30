
# Keithley S 46

## Instrument Card

S46 Microwave Switch Systems are designed to simplify the automated switching needed to test a wide range of RF and telecommunication products and devices. The S46 can control 32 relay contacts in a package as small as a 2U high (3.5 in) full-rack enclosure.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keithley Instruments is a measurement and instrument company headquartered in Solon, Ohio, that develops, manufactures, markets, and sells data acquisition products, as well as complete systems for high-volume production and assembly testing. <a href=https://www.tek.com/en>Website</a>.
<br>
<ul>
  <li>Headquarters: Cleveland, Ohio, United States</li>
  <li>Yearly Revenue (millions, USD): 110.6</li>
</ul>
</details>

## Connect to the Keithley S 46 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
from qcodes.instrument_drivers.Keithley.KeithleyS46 import KeithleyS46

# Connect to the Keithley S46 switch
s46 = KeithleyS46("s46", "TCPIP::192.168.1.1::INSTR")

# Open all channels
s46.open_all_channels()

# Close channel A1
s46.A1.set("close")

# Check if channel A1 is closed
is_closed = s46.A1.is_closed()
print(f"Channel A1 is closed: {is_closed}")
```

