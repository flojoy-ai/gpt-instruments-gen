
# Shamrock 750

## Instrument Card

The Andor Shamrock SR-750 is based on Czerny-Turner optical design. The Shamrock is available as a pre-aligned detector/spectrometer option allowing for seamless integration of software, electronics, optics and detector. There is also a fast and interactive graphical software interface allowing full control of all the spectrograph functions.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Leaders In The Development & Manufacture of Cameras, Microscopy and Spectroscopy Systems. <a href=https://andor.oxinst.com/>Website</a>.

<ul>
  <li>Headquarters: UK</li>
  <li>Yearly Revenue (millions, USD): 230.0</li>
</ul>
</details>

## Connect to the Shamrock 750 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a Shamrock 750 spectrometer using Qcodes Community, you can use the following Python script:

```python
from qcodes import Station
from qcodes.instrument_drivers.shamrock.shamrock import Shamrock_SR750

# Create a station to hold the instrument
station = Station()

# Create an instance of the Shamrock_SR750 instrument
shamrock = Shamrock_SR750('shamrock', dll_path='C:\\Program Files\\Andor SDK\\Shamrock64\\ShamrockCIF.dll', device_id=0)

# Add the instrument to the station
station.add_component(shamrock)

# Connect to the instrument
shamrock.connect()

# Now you can use the instrument methods to control the Shamrock spectrometer
# For example, you can get the current grating:
current_grating = shamrock.grating()

# Or set the wavelength:
shamrock.wavelength(500)

# Disconnect from the instrument
shamrock.disconnect()
```

Note that you need to provide the correct `dll_path` for the ShamrockCIF.dll file. Also, make sure you have the necessary dependencies installed, such as `qcodes` and `pywin32`.

