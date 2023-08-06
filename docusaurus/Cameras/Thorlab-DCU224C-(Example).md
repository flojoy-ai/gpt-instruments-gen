
# Thorlab DCU224C (Example)

## Instrument Card

DCU224C - CCD Camera, 1280 x 1024 Resolution, Color, USB 2.0

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Thorlabs, Inc. is an American privately held optical equipment company headquartered in Newton, New Jersey. The company was founded in 1989 by Alex Cable, who serves as its current president and CEO. As of 2018, Thorlabs has annual sales of approximately $500 million. <a href=https://www.thorlabs.com/>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 550.0</li>
</ul>
</details>

## Connect to the Thorlab DCU224C (Example) in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumental

To connect to a Thorlabs DCU224C camera using Instrumental, you can use the following Python script:

```python
from instrumental import instrument, list_instruments

# List all available instruments
print(list_instruments())

# Connect to the Thorlabs DCU224C camera
cam = instrument('Thorlabs DCU224C')

# Perform operations on the camera
# For example, capture an image
image = cam.grab_image()

# Close the camera connection
cam.close()
```

This script first lists all available instruments using the `list_instruments()` function from Instrumental. Then, it connects to the Thorlabs DCU224C camera using the `instrument()` function and assigns it to the `cam` variable. You can then perform operations on the camera, such as capturing an image using the `grab_image()` method. Finally, the camera connection is closed using the `close()` method.

Note that you may need to install the `instrumental` package before running this script. You can install it using pip:

```
pip install instrumental
```

Make sure you have the necessary drivers and dependencies installed for the Thorlabs DCU224C camera to work properly.

