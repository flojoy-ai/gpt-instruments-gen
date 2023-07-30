
# Lakeshore 331

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

## Connect to the Lakeshore 331 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments.lakeshore import LakeShore331

# Create a VISA adapter for communication
adapter = VISAAdapter("GPIB::1")

# Connect to the Lakeshore 331 Temperature Controller
controller = LakeShore331(adapter)

# Access the properties and methods of the controller
print(controller.output_1.setpoint)         # Print the current setpoint for loop 1
controller.output_1.setpoint = 50           # Change the loop 1 setpoint to 50 K
controller.output_1.heater_range = 'low'    # Change the heater range to low.
controller.input_A.wait_for_temperature()   # Wait for the temperature to stabilize.
print(controller.input_A.temperature)       # Print the temperature at sensor A

# Close the connection to the controller
controller.disconnect()
```

This script first creates a `VISAAdapter` object to establish communication with the Lakeshore 331 Temperature Controller using the GPIB address "GPIB::1". Then, it creates a `LakeShore331` object, passing the adapter as an argument.

The script then demonstrates how to interact with the controller by accessing its properties and methods. It prints the current setpoint for loop 1, changes the setpoint to 50 K, changes the heater range to low, waits for the temperature at sensor A to stabilize, and finally prints the temperature at sensor A.

Finally, the script closes the connection to the controller by calling the `disconnect()` method.

Note: Make sure you have the necessary dependencies installed, such as `pymeasure` and the appropriate VISA library for your instrument.

