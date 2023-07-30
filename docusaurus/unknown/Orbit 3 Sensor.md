
# Orbit 3 Sensor

## Instrument Card

Orbit 3 is a wireless sensor for ambient temperature and humidity monitoring. Install Orbit 3 at a suitable location, and it will wirelessly transmit temperature and humidity readings continuously. It can be used in precast factories, concrete laboratories, on-site – or wherever ambient climate creates value for you.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Unable to find Vendor Description. <a href=nan>Website</a>.
<br><br>
<ul>
  <li>Headquarters: nan</li>
  <li>Yearly Revenue (millions, USD): nan</li>
</ul>
</details>

## Connect to the Orbit 3 Sensor in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pytango

```python
import PyTango

# Create a DeviceProxy object to connect to the Orbit 3 Sensor
device_proxy = PyTango.DeviceProxy("device_name")

# Read a Tango attribute from the device
attribute_value = device_proxy.read_attribute("attribute_name").value

# Write a Tango attribute on the device
device_proxy.write_attribute("attribute_name", attribute_value)

# Call a Tango command on the device
device_proxy.command_inout("command_name", command_argument)
```

In the code above, replace "device_name" with the actual name of the Orbit 3 Sensor device you want to connect to. Replace "attribute_name" with the name of the attribute you want to read or write, and replace "command_name" with the name of the command you want to call. Replace "command_argument" with the argument value for the command, if applicable.

