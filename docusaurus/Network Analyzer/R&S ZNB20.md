
# R&S ZNB20

## Instrument Card

The R&S ZNB20 from R&S is a mid range vector network analyzer with two or four test ports for the frequency range from 100 kHz to 20 GHz. It has a dynamic range of 135 dB which makes it possible to perform precise measurements on wideband DUTs or components whose behavior at low frequencies is especially important. The analyzer has a large 12.1 inches touch screen interface which makes it easy to control and review test results. The ports on the R&S 20 have 2.92 mm Male connectors.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Rohde & Schwarz GmbH & Co KG is an international electronics group specializing in the fields of electronic test equipment, broadcast & media, cybersecurity, radiomonitoring and radiolocation, and radiocommunication. <a href=https://www.rohde-schwarz.com/ca/home_48230.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: Munich, Germany</li>
  <li>Yearly Revenue (millions, USD): 2500.0</li>
</ul>
</details>

## Connect to the R&S ZNB20 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

The provided code is importing the `ZNB` class from the `ZNB` module and assigning it to the variable `ZNB20`. This is done to ensure backwards compatibility with older code that might be using the `ZNB20` name.

To connect to a R&S ZNB20 Network Analyzer using Qcodes, you can use the following code:

```python
from qcodes.instrument_drivers.rohde_schwarz.ZNB.ZNB import ZNB

# Create an instance of the ZNB20 Network Analyzer
znb = ZNB('znb', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Connect to the instrument
znb.connect()
```

In the above code, we import the `ZNB` class from the `qcodes.instrument_drivers.rohde_schwarz.ZNB.ZNB` module. Then, we create an instance of the `ZNB` class with the desired name (`znb`) and the appropriate address (`TCPIP0::192.168.1.1::inst0::INSTR`). Finally, we call the `connect()` method to establish a connection with the instrument.

