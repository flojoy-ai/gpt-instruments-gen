
# Newmark - NSC-A1


## Instrument Card

The NSC-A1 Series motion controller is a powerful single axis stepper motor control system which combines a microstepping driver with a programmable controller into a compact envelope

<details open>
<summary><h2>Manufacturer Card</h2></summary>
**Newmark Systems** is a world leader in precision rotary table technology designed for critical positioning applications. <a href=https://www.newmarksystems.com/>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 12.0</li>
</ul>
</details>

## Connect to the Newmark - NSC-A1
 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumental

Here is a Python script that uses Instrumental to connect to a Newmark - NSC-A1 Motion:

```python
from instrumental import instrument, list_instruments

# Find available instruments
instruments = list_instruments()
print("Available instruments:", instruments)

# Connect to the Newmark - NSC-A1 Motion
motion = instrument('NSCA1')

# Set the angle of the rotation stage
motion.angle = 45  # Set the angle to 45 degrees

# Rotate clockwise by a specified angle
motion.cw(90)  # Rotate clockwise by 90 degrees

# Rotate counter-clockwise by a specified angle
motion.ccw(180)  # Rotate counter-clockwise by 180 degrees

# Get the current angle of the rotation stage
current_angle = motion.angle
print("Current angle:", current_angle)

# Set the velocity of the rotation stage
motion.velocity = 10  # Set the velocity to 10 degrees per second

# Get the current velocity of the rotation stage
current_velocity = motion.velocity
print("Current velocity:", current_velocity)

# Close the connection to the Newmark - NSC-A1 Motion
motion.close()
```

Note: This script assumes that you have already installed the `instrumental` package and have the necessary dependencies installed.

