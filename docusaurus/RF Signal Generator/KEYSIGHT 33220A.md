
# KEYSIGHT 33220A

## Instrument Card

The Keysight 33220A is a 20 MHz synthesized function generator with built-in arbitrary waveform and pulse capabilities. Itscombination of bench-top and system features makes this function generator a versatile solution for your testing requirements now and in the future.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 33220A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit


```python
from instrumentkit import Instrument, SCPIInstrument

# Define the SCPI commands for the KEYSIGHT 33220A RF Signal Generator
class Keysight33220A(SCPIInstrument):
    def __init__(self, resource_name):
        super().__init__(resource_name)
    
    def set_frequency(self, frequency):
        self.send_command(f"FREQ {frequency}")
    
    def set_amplitude(self, amplitude):
        self.send_command(f"VOLT {amplitude}")
    
    def enable_output(self):
        self.send_command("OUTP ON")
    
    def disable_output(self):
        self.send_command("OUTP OFF")

# Connect to the KEYSIGHT 33220A RF Signal Generator
signal_generator = Keysight33220A("TCPIP0::192.168.1.1::INSTR")

# Set the frequency to 1 MHz
signal_generator.set_frequency(1e6)

# Set the amplitude to 1 Vpp
signal_generator.set_amplitude(1)

# Enable the output
signal_generator.enable_output()

# Disable the output after 5 seconds
time.sleep(5)
signal_generator.disable_output()

# Disconnect from the signal generator
signal_generator.disconnect()
```

Make sure to replace `"TCPIP0::192.168.1.1::INSTR"` with the actual resource name or address of your KEYSIGHT 33220A RF Signal Generator.

