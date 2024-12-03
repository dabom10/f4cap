from gpiozero import MCP3008
from time import sleep

adc_channel = 0


light_sensor = MCP3008(channel=adc_channel, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=5)

print("roading...")

try:
    while True:
        adc_value = light_sensor.value
        
        raw_value = int(adc_value * 1023)

        print(f"ADC: {adc_value:.2f}, RAW: {raw_value}")
        
        sleep(0.5)
except KeyboardInterrupt:
    print("the end")
