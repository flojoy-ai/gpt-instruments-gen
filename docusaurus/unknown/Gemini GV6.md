
# Gemini GV6

## Instrument Card

Incorporates all of the powerful features of the Gemini GV digital servo drive
Provides six power ranges for up to 11.8 kW of continuous power
Stand-alone servo controller and drive in one small package
Full ASCII communications capability
Control features such as registration, motion profiles, S-curve velocity profiling and conditional statements
Program storage: Up to 32 programs or 190 lines of program code
Daisy chain up to 99 units
Simplified configuration and tuning
8 programmable inputs and 6 programmable outputs
Wide range of PWM frequencies for linear motor support

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Parker Hannifin Corporation, originally Parker Appliance Company, usually referred to as just Parker, is an American corporation specializing in motion and control technologies. <a href=https://www.parker.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 18000.0</li>
</ul>
</details>

## Connect to the Gemini GV6 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.instruments.parker import ParkerGV6

# Create an instance of the ParkerGV6 instrument
motor = ParkerGV6("ASRL1::INSTR")

# Connect to the motor controller
motor.connect()

# Enable the motor
motor.enable()

# Set the motor velocity to 5 revolutions per second
motor.velocity = 5

# Move the motor to a specific angle
motor.angle = 90

# Check if the motor is currently moving
is_moving = motor.is_moving()

# Disable the motor
motor.disable()

# Disconnect from the motor controller
motor.disconnect()
```

This script creates an instance of the `ParkerGV6` instrument, connects to the motor controller using the specified address (e.g., `"ASRL1::INSTR"`), enables the motor, sets the velocity, moves the motor to a specific angle, checks if the motor is moving, disables the motor, and finally disconnects from the motor controller.

