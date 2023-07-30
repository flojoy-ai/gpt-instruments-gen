
# Keysight 3456A

## Instrument Card

3456A 6 1/2 Digit Digital Multimeter

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the Keysight 3456A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit


```python
import instrumentkit as ik

# Connect to the multimeter
multimeter = ik.keysight.Keysight3456A.open_gpibusb("/dev/ttyUSB0", 22)

# Set the measurement mode to DC voltage
multimeter.mode = multimeter.Mode.dcv

# Perform a measurement
measurement = multimeter.measure()

# Print the measurement result
print(f"Measurement: {measurement}")
```

In this script, we first import the `instrumentkit` module and then use the `open_gpibusb` method of the `ik.keysight.Keysight3456A` class to connect to the multimeter. You'll need to replace `"/dev/ttyUSB0"` with the appropriate device path for your system.

Next, we set the measurement mode to DC voltage by assigning the `multimeter.Mode.dcv` value to the `mode` property of the multimeter object.

Finally, we use the `measure` method of the multimeter object to perform a measurement and store the result in the `measurement` variable. We then print the measurement result.

Note that this script assumes you have already installed the `instrumentkit` library. If not, you can install it using `pip install instrumentkit`.

