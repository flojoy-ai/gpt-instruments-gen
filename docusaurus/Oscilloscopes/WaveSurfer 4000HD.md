
# WaveSurfer 4000HD

## Instrument Card

WaveSurfer 4000HD extends Teledyne LeCroy’s leadership in High Definition Oscilloscopes with a bright, 12.1” touch screen display, performance without compromise, and price points that fit your budget.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Teledyne LeCroy is an American manufacturer of oscilloscopes, protocol analyzers and other test equipment. LeCroy is now a subsidiary of Teledyne Technologies. <a href=https://www.teledynelecroy.com/>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5458.6</li>
</ul>
</details>

## Connect to the WaveSurfer 4000HD in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

To connect to a WaveSurfer 4000HD Oscilloscope using Instrumentkit, you can use the following code:

```python
import instrumentkit as ik

# Connect to the oscilloscope
oscilloscope = ik.teledyne.MAUI.open_visa("TCPIP0::192.168.0.10::INSTR")

# Perform operations on the oscilloscope
# For example, you can read the waveform from a channel
channel = oscilloscope.channel[0]
xdat, ydat = channel.read_waveform()

# Print the waveform data
print("X Data:", xdat)
print("Y Data:", ydat)

# Close the connection to the oscilloscope
oscilloscope.close()
```

This code connects to the oscilloscope at the specified IP address ("TCPIP0::192.168.0.10::INSTR") using the VISA protocol. It then reads the waveform data from the first channel and prints it. Finally, it closes the connection to the oscilloscope.

Note: Make sure to replace "TCPIP0::192.168.0.10::INSTR" with the actual IP address of your WaveSurfer 4000HD Oscilloscope.

