
# Keithley 6221

## Instrument Card

The 6221 AC and DC Current Source combine ease of use with exceptionally low current noise. Low current sourcing is critical to applications in test environments ranging from R&D to production, especially in the semiconductor, nanotechnology, and superconductor industries. High sourcing accuracy and built-in control functions make the 6221 ideal for applications like Hall measurements, resistance measurements using delta mode, pulsed measurements, and differential conductance measurements.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keithley Instruments is a measurement and instrument company headquartered in Solon, Ohio, that develops, manufactures, markets, and sells data acquisition products, as well as complete systems for high-volume production and assembly testing. <a href=https://www.tek.com/en>Website</a>.
<br></br>
<ul>
  <li>Headquarters: Cleveland, Ohio, United States</li>
  <li>Yearly Revenue (millions, USD): 110.6</li>
</ul>
</details>

## Connect to the Keithley 6221 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure

Here is a Python script that uses Pymeasure to connect to a Keithley 6221 Power Supply:

```python
from pymeasure.instruments.keithley import Keithley6221

# Connect to the Keithley 6221
keithley = Keithley6221("GPIB::1")

# Enable the source
keithley.enable_source()

# Set the source current to 0.05 Amps
keithley.source_current = 0.05

# Set the source compliance to 10 Volts
keithley.source_compliance = 10

# Set the waveform function to square
keithley.waveform_function = "square"

# Set the waveform amplitude to 0.05 Amps
keithley.waveform_amplitude = 0.05

# Set the waveform offset to 0 Amps
keithley.waveform_offset = 0

# Set the waveform frequency to 347 Hz
keithley.waveform_frequency = 347

# Set the waveform duty cycle to 50%
keithley.waveform_dutycycle = 50

# Set the waveform ranging to "best"
keithley.waveform_ranging = "best"

# Set the waveform duration in cycles to 100
keithley.waveform_duration_cycles = 100

# Arm (load) the waveform
keithley.waveform_arm()

# Start the waveform
keithley.waveform_start()

# Wait for the waveform to finish
keithley.adapter.wait_for_srq()

# Disarm (unload) the waveform
keithley.waveform_abort()

# Disable the source
keithley.disable_source()

# Close the connection to the Keithley 6221
keithley.shutdown()
```

This script connects to the Keithley 6221 using the GPIB interface (address "GPIB::1"). It enables the source, sets the source current and compliance, and configures the waveform parameters. It then arms and starts the waveform, waits for it to finish using the Service Request (SRQ) event, and aborts the waveform. Finally, it disables the source and closes the connection to the Keithley 6221.

