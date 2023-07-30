
# PCO Pixelfly

## Instrument Card

The pco.pixelfly™ 1.3 SWIR is a high-performance machine vision camera due to its special InGaAs image sensor which is sensitive in the shortwave infrared, near infrared and visible range of the electromagnetic spectrum.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
**PCO** is one of the leading manufacturers of scientific **cameras**: sCMOS & Highspeed **camera** systems, developed and produced in Kelheim Bavaria Germany. <a href=https://www.pco-tech.com>Website</a>.

<ul>
  <li>Headquarters: Germany</li>
  <li>Yearly Revenue (millions, USD): 7.0</li>
</ul>
</details>

## Connect to the PCO Pixelfly in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumental

To connect to a PCO Pixelfly camera using Instrumental, you can use the following code:

```python
from instrumental import instrument, list_instruments

# List all available PCO Pixelfly cameras
cameras = list_instruments('Pixelfly')

# Connect to the first camera
camera = instrument(cameras[0])

# Perform camera operations
# ...

# Close the camera connection
camera.close()
```

This code uses the `instrumental` library to list all available PCO Pixelfly cameras using the `list_instruments` function. It then connects to the first camera in the list using the `instrument` function. You can perform camera operations using the `camera` object, and finally, close the camera connection using the `close` method.

