
# Attocube ECC 100

## Instrument Card

The ECC100 is a state-ofthe-art motion controller, allowing the simultaneous operation of up to three positioners from attocube’s industrial ECS Drive series.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
**Attocube** is a leading pioneer for nanotechnology solutions in precision motion and nanopositioning applications, cryogenic microscopy,. <a href=https://www.attocube.com/en>Website</a>.

<ul>
  <li>Headquarters: Germany</li>
  <li>Yearly Revenue (millions, USD): 14.0</li>
</ul>
</details>

## Connect to the Attocube ECC 100 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumental

To connect to an Attocube ECC 100 Motion using Instrumental, you can use the following Python script:

```python
from instrumental import instrument, list_instruments

# List all available instruments
instruments = list_instruments()
print(instruments)

# Connect to the Attocube ECC 100 Motion
ecc100 = instrument(instruments[0])

# Get the current position of the linear stage
position = ecc100.get_position()
print("Current position:", position)

# Move the linear stage to a new position
new_position = 100  # Replace with the desired position
ecc100.move_to(new_position, wait=True)

# Get the target position of the linear stage
target_position = ecc100.get_target()
print("Target position:", target_position)

# Disconnect from the Attocube ECC 100 Motion
ecc100.close()
```

Note: Make sure to replace `instruments[0]` with the appropriate instrument name from the `list_instruments()` output.

