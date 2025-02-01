# **plantbot**

## **What is plantbot?**
This is a bot that allows members of a Discord server to check in on and water a plant of mine.

The bot listens for commands in a certain channel of the Discord server. It's run on a Raspberry Pi Zero 2 W with the following hat/sensors onboard:
- a [Pimoroni Grow hat](https://shop.pimoroni.com/products/grow?variant=32208365486163) with [moisture sensors](https://shop.pimoroni.com/products/grow-moisture-sensor-pack-of-3?variant=32271401123923) and [pumps](https://shop.pimoroni.com/products/mini-pump?variant=39273944907859)
- a [BME680 sensor](https://shop.pimoroni.com/products/bme680-breakout?variant=12491552129107)
- a [Camera Module 3](https://shop.pimoroni.com/products/raspberry-pi-camera-module-3?variant=40448391774291) with [camera cable](https://shop.pimoroni.com/products/camera-cable-raspberry-pi-zero-edition?variant=32092803891283)

## **Commands:**
- `!pic` - takes a picture and sends it to the channel.
- `!enviro` - sends a temperature reading of the room to the channel from the BME680
- `!moisture` - collects a moisture reading and sends it to the channel
- `!water` - activates water pump that waters the plant for a set amount of time (will not activate if the moisture is above a value, to prevent overwatering)

## **Required Packages & Libraries:**
For plantbot to live, it will need the following packages installed:
- `discord.py` – [GitHub](https://github.com/Rapptz/discord.py) // [Docs](https://discordpy.readthedocs.io/en/stable/index.html#)
- `Grow Hat` - [GitHub](https://github.com/pimoroni/grow-python) // [Getting started doc](https://learn.pimoroni.com/article/assembling-grow#introduction)
- `picamera2` – [Doc](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)
- `bme680` – [PyPI](https://pypi.org/project/bme680/)