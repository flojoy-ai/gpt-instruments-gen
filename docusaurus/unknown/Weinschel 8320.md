
# Weinschel 8320

## Instrument Card

Spectrum Control's Weinschel brand Model 8320 Series Multi-channel Programmable Attenuator systems allow for multiple attenuator channels to be controlled across a variety of interfaces, or via a front panel.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Weinschel Associates designs and manufactures high-quality Broadband RF and Microwave products for commercial and military markets domestically and internationally. Core technologies originated by founder Bruno Weinschel are leveraged using modern design, production, delivery, and service techniques to provide the best product at the best price to our customers. <a href=https://www.weinschelassociates.com/>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 6.6</li>
</ul>
</details>

## Connect to the Weinschel 8320 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here's a Python script that uses Qcodes to connect to a Weinschel 8320 attenuator:

```python
from qcodes.instrument.visa import VisaInstrument

# Create an instance of the Weinschel8320 instrument
weinschel = Weinschel8320('weinschel', 'your_visa_address')

# Connect to the instrument
weinschel.connect()

# Set the attenuation to 10 dB
weinschel.attenuation(10)

# Get the current attenuation value
attenuation_value = weinschel.attenuation()

# Print the current attenuation value
print(f"Current attenuation: {attenuation_value} dB")

# Disconnect from the instrument
weinschel.disconnect()
```

Note: Replace `'your_visa_address'` with the actual VISA address of your Weinschel 8320 attenuator.

