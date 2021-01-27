# -*- coding: utf-8 -*-

import evdev, asyncio, pprint

ps3dev = []

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if 'PLAYSTATION(R)3' in device.name:
        ps3dev.append(device)
        print(device)
        pprint.pprint(device.capabilities(verbose=True, absinfo=True))

async def print_events(device):
    async for event in device.async_read_loop():
        print(device.path, evdev.categorize(event), sep=' >> ')

for device in ps3dev:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()
