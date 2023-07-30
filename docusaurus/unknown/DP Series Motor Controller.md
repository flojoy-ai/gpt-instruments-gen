
# DP Series Motor Controller

## Instrument Card



<details open>
<summary><h2>Manufacturer Card</h2></summary>
Unable to find Vendor Description. <a href=nan>Website</a>.

<ul>
  <li>Headquarters: nan</li>
  <li>Yearly Revenue (millions, USD): nan</li>
</ul>
</details>

## Connect to the DP Series Motor Controller in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import SerialAdapter
from pymeasure.instruments import DPSeriesMotorController

# Create a SerialAdapter for communication with the motor controller
adapter = SerialAdapter(port='COM1', baudrate=38400)

# Create an instance of the DPSeriesMotorController
motor_controller = DPSeriesMotorController(adapter)

# Set the motor controller's address
motor_controller.address = 1

# Move the motor in the clockwise direction
motor_controller.move('CW')

# Wait for the motor to complete the movement
motor_controller.wait_for_completion()

# Stop the motor
motor_controller.stop()

# Read the current motor position in steps
position = motor_controller.step_position
print("Current position:", position)

# Reset the motor position to 0
motor_controller.reset_position()

# Close the connection to the motor controller
motor_controller.close()
```

This script connects to a DP Series Motor Controller using a SerialAdapter and creates an instance of the DPSeriesMotorController class. It then sets the motor controller's address, moves the motor in the clockwise direction, waits for the motor to complete the movement, stops the motor, reads the current motor position in steps, resets the motor position to 0, and finally closes the connection to the motor controller.

