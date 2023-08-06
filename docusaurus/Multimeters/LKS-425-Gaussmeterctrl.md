
# LKS 425 Gaussmeterctrl

## Instrument Card

Class Connecting To The Lakeshore 425 Gaussmeter

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Supporting advanced scientific research, Lake Shore is a leading global innovator in measurement and control solutions. <a href=https://www.lakeshore.com/home>Website</a>.
<br><br>
<ul>
  <li>Headquarters: Westerville, Ohio, USA</li>
  <li>Yearly Revenue (millions, USD): 21.4</li>
</ul>
</details>

## Connect to the LKS 425 Gaussmeterctrl in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pytango

To connect to a LKS 425 Gaussmeterctrl Multimeters using Pytango, you can use the following code:

```python
import PyTango

# Create a DeviceProxy for the Gaussmeterctrl Multimeters
device_proxy = PyTango.DeviceProxy("device_name")

# Connect to the device
device_proxy.Connect()

# Check if the device is connected
if device_proxy.State() == PyTango.DevState.ON:
    print("Device is connected")
else:
    print("Device is not connected")

# Disconnect from the device
device_proxy.Disconnect()
```

Replace `"device_name"` with the actual name of the device you want to connect to.

