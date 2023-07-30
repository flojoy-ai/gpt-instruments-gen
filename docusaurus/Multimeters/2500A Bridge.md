
# 2500A Bridge

## Instrument Card

The AH 2500A offers unparalleled stability, resolution and accuracy in a capacitance/loss1 bridge (whether manual or automatic)

<details open>
<summary><h2>Manufacturer Card</h2></summary>
**Andeen**-**Hagerling**, Inc. - manufacturers of the world's most accurate capacitance bridges and standards. <a href=http://www.andeen-hagerling.com/>Website</a>.

<ul>
  <li>Headquarters: US</li>
  <li>Yearly Revenue (millions, USD): 1.0</li>
</ul>
</details>

## Connect to the 2500A Bridge in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments import AH2500A

# Create a VISA adapter for communication
adapter = VISAAdapter("GPIB0::1::INSTR")

# Connect to the AH2500A instrument
bridge = AH2500A(adapter)

# Perform a single capacitance and loss measurement
capacitance, loss, voltage = bridge.caplossvolt

# Print the measurement values
print(f"Capacitance: {capacitance} pF")
print(f"Loss: {loss} nS")
print(f"Voltage: {voltage} V")

# Disconnect from the instrument
bridge.disconnect()
```

This script connects to the AH2500A instrument using a VISA adapter, performs a single capacitance and loss measurement, and prints the measurement values. Finally, it disconnects from the instrument.

