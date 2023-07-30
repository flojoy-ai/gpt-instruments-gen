
# Model 331

## Instrument Card

The Model 331 cryogenic temperature controller combines the easy operation and unsurpassed reliability of the Model 330 with improved sensor input and interface flexibility, including compatibility with negative temperature coefficient (NTC) resistance temperature detectors (RTDs). Backed by the Lake Shore tradition of excellence in cryogenic sensors and instrumentation, the Model 331 temperature controller sets the standard for mid-price range temperature control instruments.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Supporting advanced scientific research, Lake Shore is a leading global innovator in measurement and control solutions. <a href=https://www.lakeshore.com/home>Website</a>.
<br><br>
<ul>
  <li>Headquarters: Westerville, Ohio, USA</li>
  <li>Yearly Revenue (millions, USD): 21.4</li>
</ul>
</details>

## Connect to the Model 331 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a Model 331 Temperature Controller using Qcodes Community, you can use the following Python script:

```python
from qcodes import Station
from qcodes.instrument_drivers.Lakeshore.Model_331 import Model_331

# Create a station to hold the instrument
station = Station()

# Connect to the Model 331 Temperature Controller
model_331 = Model_331('model_331', 'GPIB0::1::INSTR')
station.add_component(model_331)

# Print the heater output
print(model_331.heater_output())

# Set the heater range to 5W
model_331.heater_range('5W')

# Print the temperature of channel A
print(model_331.channels.ChanA.temperature())

# Set the setpoint temperature to 300K for channel B
model_331.channels.ChanB.setpoint(300)

# Disconnect from the instrument
model_331.close()
```

This script creates a `Station` object to hold the instrument and then connects to the Model 331 Temperature Controller using the `Model_331` class. The instrument is added to the station using the `add_component` method.

You can then use the instrument's parameters and methods to interact with the instrument. In the provided example, the script prints the heater output, sets the heater range, prints the temperature of channel A, and sets the setpoint temperature for channel B.

Finally, the script closes the connection to the instrument using the `close` method.

