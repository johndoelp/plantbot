# plantbot
This is a bot that allows members of a Discord server to check in on a plant of mine.

The Discord bot listens for commands in a certain channel of the Discord server. It's run on a Raspberry Pi Zero W 2 with a Pimoroni Grow hat and BME680.

Commands include:
- "/pic": takes a picture using a Raspberry Pi Camera Module 3 Wide camera sensor, and sends it to the channel.
- "/enviro": sends a temperature reading of the room to the channel from the onboard BME680
- "/moist": collects moisture reading from a moisture sensor connected to the Pimoroni Grow hat and sends it to the channel
- "/water": activates water pump that waters the plant for a set amount of time. This command cannot be used if the mosture of the soil is above a nominal value, to avoid overwatering