
# Newportesp 301

## Instrument Card

The ESP301-3N 3 Axis Motion Controller and Driver is the successor of the popular ESP300 motion controller. The ESP301 provides the same functionality as the ESP300 with a standard USB interface and extended front panel functions. For maximum backward compatibility, the ESP301 features the same motion commands and control algorithms and the same casing as the ESP300. The ESP301-3N drives and controls up to three axes of motion using any combination of DC or 2-phase stepper motors up to 3A per axis. This capability enables driving a large selection of Newport stages and actuators. Featuring an integrated manual front panel interface and Newport's unique ESP stage auto-detection and auto-configuration, the ESP301 provides most easy operation and excellent functionality at an affordable price.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Newport provides a wide range of photonics technology and products designed to enhance the capabilities and productivity of our customers' applications. <a href=https://www.newport.com/>Website</a>.
<br>
<ul>
  <li>Headquarters: Irvine, California, United States</li>
  <li>Yearly Revenue (millions, USD): 3500.0</li>
</ul>
</details>

## Connect to the Newportesp 301 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

To connect to a Newport ESP-301 Positional Controller using Instrumentkit, you can use the following code:

```python
from instrumentkit import NewportESP301

# Connect to the controller
controller = NewportESP301.open_serial("COM3")

# Access the axis of the controller
axis = controller.axis[0]

# Move the axis to a specific position
axis.move(0.001, absolute=False)

# Wait for the motion to finish
axis.wait_for_motion()

# Disconnect from the controller
controller.close()
```

This code connects to the Newport ESP-301 controller using the `open_serial` method, which takes the serial port as an argument. It then accesses the first axis of the controller using `controller.axis[0]`. You can perform various operations on the axis, such as moving it to a specific position using the `move` method, waiting for the motion to finish using the `wait_for_motion` method, and closing the connection using the `close` method.

