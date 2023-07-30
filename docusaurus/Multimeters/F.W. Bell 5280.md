
# F.W. Bell 5280

## Instrument Card

Handheld single-axis digital magnetometer gauss / tesla meter for measuring magnets, magnetism of steel, and other manufacturing and scientific applications.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Technology leaders in instrumentation. Designing and manufacturing **F.W. Bell** gaussmeters, probes, current sensors and Hall generators for over 60 years. <a href=https://fwbell.com/>Website</a>.
<br>
<ul>
  <li>Headquarters: UK (Meggit)</li>
  <li>Yearly Revenue (millions, USD): nan</li>
</ul>
</details>

## Connect to the F.W. Bell 5280 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.instruments import SerialInstrument
from pymeasure.adapters import SerialAdapter

# Create a SerialAdapter for the instrument
adapter = SerialAdapter(port='/dev/ttyUSB0', baudrate=2400)

# Create a SerialInstrument using the adapter
meter = SerialInstrument(adapter)

# Open the connection to the instrument
meter.open()

# Set the measurement units to Gauss
meter.write(":UNIT:FLUX:DC:GAUSS")

# Set the range to 3 kG
meter.write(":SENS:FLUX:RANG 1")

# Read and print a field measurement in G
field = meter.query(":MEASure:FLUX?")
print("Field measurement:", field)

# Close the connection to the instrument
meter.close()
```

This script connects to the F.W. Bell 5080 Handheld Gaussmeter using a SerialAdapter and SerialInstrument from Pymeasure. It sets the measurement units to Gauss and the range to 3 kG, then reads and prints a field measurement in G. Finally, it closes the connection to the instrument.

