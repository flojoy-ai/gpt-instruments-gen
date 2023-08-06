
# Lakeshore Model 336

## Instrument Card

The Model 336 supports the industry’s most advanced line of cryogenic temperature sensors as manufactured by Lake Shore, including diodes, resistance temperature detectors (RTDs), and thermocouples. The controller’s zone tuning feature allows you to measure and control temperatures seamlessly from 300 mK to over 1,500 K by automatically switching temperature sensor inputs when your temperature range goes beyond the usable range of a given sensor.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Supporting advanced scientific research, Lake Shore is a leading global innovator in measurement and control solutions. <a href=https://www.lakeshore.com/home>Website</a>.
<br></br>
<ul>
  <li>Headquarters: Westerville, Ohio, USA</li>
  <li>Yearly Revenue (millions, USD): 21.4</li>
</ul>
</details>

## Connect to the Lakeshore Model 336 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a Lakeshore Model 336 Temperature Controller using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Lakeshore.Model336 import Model336

# Create an instance of the Model336 instrument
lakeshore = Model336("lakeshore", "TCPIP::192.168.1.1::7777::SOCKET")

# Connect to the instrument
lakeshore.connect()

# Now you can use the instrument to perform various operations
# For example, you can read the temperature from a sensor
temperature = lakeshore.temperature()

# You can also set the temperature setpoint
lakeshore.temperature_setpoint(300)

# Disconnect from the instrument
lakeshore.disconnect()
```

Note that you need to replace `"TCPIP::192.168.1.1::7777::SOCKET"` with the actual IP address and port of your Lakeshore Model 336 Temperature Controller.

