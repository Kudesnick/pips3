# -*- coding: utf-8 -*-

import evdev, asyncio, pprint, sys
from pathlib import Path

ps3dev = []
ev_key = dict()
ev_abs = dict()

devices = [evdev.InputDevice(path) for path in sorted(evdev.list_devices())]
for device in devices:
    if 'PLAYSTATION(R)3' in device.name:
        ps3dev.append(device)
    else:
        device.close()

for device in ps3dev:
    print(device)
    # pprint.pprint(device.capabilities(verbose=True, absinfo=True))
    caps = device.capabilities(verbose=False, absinfo=False)
    
    klist = caps.get(evdev.ecodes.ecodes['EV_KEY'])
    if klist != None:
        ev_key[str(device.path)] = {i: 0 for i in klist}
        #print(ev_key[device.path])
    
    alist = caps.get(evdev.ecodes.ecodes['EV_ABS'])
    if alist != None:
        ev_abs[str(device.path)] = {i: device.absinfo(i).value for i in alist}
        #print(ev_abs[device.path])

bat = list(Path('/sys/class/power_supply').glob('sony_controller_battery_*'))[0] / Path('capacity')
with open(str(bat), 'r') as f:
    print('battery: {}%'.format(f.readline().strip()))

def jprint(_sep: str = ';', _end: str = '\r'):
    global ev_key, ev_abs

    print(_sep.join([str(i) for j in ev_key.values() for i in j.values()]),
          _sep.join([str(i).zfill(4) for j in ev_abs.values() for i in j.values()]),
          sep = _sep + _sep,
          end = _end
          )

jprint()

async def print_events(device):
    async for event in device.async_read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            ev_key[str(device.path)][event.code] = event.value
            #print(ev_key[str(device.path)])
        if event.type == evdev.ecodes.EV_ABS:
            ev_abs[str(device.path)][event.code] = event.value
            #print(ev_abs[str(device.path)])
        jprint()


for device in ps3dev:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()

_old_excepthook = sys.excepthook
def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print()
        #ctl+C reaction
        loop.stop()
    else:
        _old_excepthook(exctype, value, traceback)
sys.excepthook = myexcepthook

loop.run_forever()
loop.close()
