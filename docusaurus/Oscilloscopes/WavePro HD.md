
# WavePro HD

## Instrument Card

WavePro HD High-Definition oscilloscopes employ unique Teledyne LeCroy HD4096 technology to achieve 12-bit resolution at up to 8 GHz bandwidth, for the lowest noise and unmatched signal fidelity. Up to 5 Gpt of highly responsive acquisition memory gives more visibility into system behavior, and the exceptional analysis toolbox enables deep insight.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Teledyne LeCroy is an American manufacturer of oscilloscopes, protocol analyzers and other test equipment. LeCroy is now a subsidiary of Teledyne Technologies. <a href=https://www.teledynelecroy.com/>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5458.6</li>
</ul>
</details>

## Connect to the WavePro HD in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

To connect to a WavePro HD Oscilloscope using Instrumentkit, you can use the following code:

```python
import instrumentkit as ik

# Connect to the oscilloscope
oscilloscope = ik.teledyne.WaveProHD.open_visa("TCPIP0::192.168.0.10::INSTR")

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

This code connects to a WavePro HD Oscilloscope at the specified IP address ("TCPIP0::192.168.0.10::INSTR"). It then reads the waveform data from the first channel and prints it. Finally, it closes the connection to the oscilloscope.

Note: Make sure to replace "TCPIP0::192.168.0.10::INSTR" with the actual IP address of your oscilloscope.

