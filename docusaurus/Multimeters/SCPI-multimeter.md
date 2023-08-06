
# SCPI multimeter

## Instrument Card

All SCPI Multimeters

<details open>
<summary><h2>Manufacturer Card</h2></summary>
. <a href=nan>Website</a>.
<br></br>
<ul>
  <li>Headquarters: nan</li>
  <li>Yearly Revenue (millions, USD): nan</li>
</ul>
</details>

## Connect to the SCPI multimeter in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

To connect to a SCPI multimeter using Instrumentkit, you can use the following code:

```python
import instrumentkit as ik

# Connect to the multimeter
multimeter = ik.SCPIMultimeter.open_tcpip("192.168.1.1")

# Set the measurement mode to voltage DC
multimeter.mode = multimeter.Mode.voltage_dc

# Perform a measurement
measurement = multimeter.measure()

# Print the measurement result
print(measurement)
```

This code connects to the multimeter using the `open_tcpip` method, sets the measurement mode to voltage DC using the `mode` property, performs a measurement using the `measure` method, and prints the measurement result.

