
# AVS 47

## Instrument Card

The Picowatt AVS 47 is a resistance bridge used to measure the resistance of low-temperature sensors.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
RV-Elektroniikka Oy PICOWATT is specialized in manufacturing instruments for thermometry at ultralow temperatures. Founded in February 1978, we have gathered 45 years of experience in designing and manufacturing low-noise precision. <a href=https://www.picowatt.fi/index1.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: Finland</li>
  <li>Yearly Revenue (millions, USD): 5.0</li>
</ul>
</details>

## Connect to the AVS 47 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

Here is an example Python script that uses Instrumentkit to connect to a Picowatt AVS 47 resistance bridge:

```python
import instrumentkit as ik

# Connect to the AVS 47 resistance bridge
bridge = ik.picowatt.PicowattAVS47.open_gpibusb('/dev/ttyUSB0', 1)

# Set the input source to actual
bridge.input_source = bridge.InputSource.actual

# Set the multiplexer channel to 0
bridge.mux_channel = 0

# Get the resistance of the first sensor
resistance = bridge.sensor[0].resistance

# Print the resistance
print(resistance)
```

This script imports the `instrumentkit` module and uses the `open_gpibusb` method of the `PicowattAVS47` class to connect to the resistance bridge. It then sets the input source to actual and the multiplexer channel to 0. Finally, it retrieves the resistance of the first sensor using the `resistance` property of the `Sensor` class and prints it.

