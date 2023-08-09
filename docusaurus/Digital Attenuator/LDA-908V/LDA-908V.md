
# LDA-908V

## Instrument Card

<div className="flex">

<div>

The LDA-908V Digital Attenuator is a highly accurate, bidirectional, 50 Ohm step attenuator. The LDA-908V provides calibrated attenuation from 200 to 8000 MHz with an amazing step size of 0.1 dB and typical accuracy <0.25 dB over 90 dB of control range. The attenuators are easily programmable for fixed attenuation, swept attenuation ramps and fading profiles directly from the included Graphical User Interface (GUI). Alternatively, for users wishing to develop their own interface, Vaunix supplies LabVIEW drivers, Windows API DLL files, Linux drivers, Python examples and much more.

</div>

<img src={require("./LDA-908V.jpg").default} width="256" height="150"/>

</div>

The LDA-908V Digital Attenuator is a highly accurate, bidirectional, 50 Ohm step attenuator. The LDA-908V provides calibrated attenuation from 200 to 8000 MHz with an amazing step size of 0.1 dB and typical accuracy <0.25 dB over 90 dB of control range. The attenuators are easily programmable for fixed attenuation, swept attenuation ramps and fading profiles directly from the included Graphical User Interface (GUI). Alternatively, for users wishing to develop their own interface, Vaunix supplies LabVIEW drivers, Windows API DLL files, Linux drivers, Python examples and much more.>

<details open>
<summary><h2>Manufacturer Card</h2></summary>

Vaunix Technology Corp. designs, manufactures, and services RF and microwave test equipment and digital radio communications products. Utilizing our deep RF and software engineering expertise, rooted in microwave radio and wireless equipment repair and testing, Vaunix developed the Lab Brick® family of electronic test products, which set a new standard for cost, size, and simplicity of wireless testing devices. Powered by a USB connection and controlled by easy-to-use, graphical-user-interface (GUI) software, Lab Bricks have been designed to meet the needs of wireless engineers and technicians who want to create flexible, customized system solutions either in the lab or in the field. We 've expanded our Lab Brick® family of electronic test products to include Attenuator Matrix solutions that double as Wireless [Handover Test Systems](https://vaunix.com/handover-test-systems/) to give our test technicians and product engineers the advanced capability to solve unique wireless _handover _testing challenges and bring affordability, functionality, reliability and simplicity to the microwave test bench. <a href="https://vaunix.com/">Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5.0</li>
</ul>
</details>

## Connect to the LDA-908V in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a LDA-908V using Qcodes Community, you can use the following Python script:

```python
from qcodes import Station
from qcodes_contrib_drivers.drivers.Vaunix_LDA import LDA

# Create a station to hold the instruments
station = Station()

# Connect to the LDA-908V
lda = LDA('lda', serial_number=908, dll_path='path/to/dll')

# Add the LDA to the station
station.add_component(lda)

# Print the IDN of the LDA
print(lda.get_idn())

# Set the attenuation to 10 dB
lda.attenuation(10)

# Close the connection to the LDA
lda.close()
```

Make sure to replace `'path/to/dll'` with the actual path to the DLL file for the LDA-908V.
