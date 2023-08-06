
# LKS 425 Gaussmeter

## Instrument Card

Lake Shore Model 425 gaussmeter provides high-end functionality and performance in an affordable desktop instrument. Magnet testing and sorting have never been easier. When used in combination with the built-in relay and audible alarm features, the Model 425 takes the guesswork out of pass/fail criteria. Additional features including DC to 10 kHz AC frequency response, max hold and relative measurement make the Model 425 the ideal tool for your manufacturing, quality control and R&D flux density measurement applications. Put the Model 425 gaussmeter to use with confidence knowing it’s supported by industry leading experts in magnet measurement instrument, sensor, and Hall probe technology.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Supporting advanced scientific research, Lake Shore is a leading global innovator in measurement and control solutions. <a href=https://www.lakeshore.com/home>Website</a>.
<br></br>
<ul>
  <li>Headquarters: Westerville, Ohio, USA</li>
  <li>Yearly Revenue (millions, USD): 21.4</li>
</ul>
</details>

## Connect to the LKS 425 Gaussmeter in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pytango

To connect to a Lake Shore Model 425 Gaussmeter using Pytango, you can use the following code:

```python
import PyTango

# Create a DeviceProxy for the Gaussmeter
gaussmeter_proxy = PyTango.DeviceProxy("device/hostname/instance")

# Call the relevant methods on the Gaussmeter proxy
# For example, to get the serial number:
serial_number = gaussmeter_proxy.read_attribute("SerialNumber").value

# To get the current magnetic field reading:
magnetic_field = gaussmeter_proxy.read_attribute("MagneticField").value

# To set the measurement range:
gaussmeter_proxy.write_attribute("MeasurementRange", 1)

# To start a measurement:
gaussmeter_proxy.command_inout("StartMeasurement")

# To stop a measurement:
gaussmeter_proxy.command_inout("StopMeasurement")
```

Note that you need to replace `"device/hostname/instance"` with the actual Tango device name or alias for your Lake Shore Model 425 Gaussmeter.

