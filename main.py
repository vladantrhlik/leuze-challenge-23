import telnetlib

from modules.scroll_wheel import ScrollWheel
from modules.melody_player import MelodyPlayer
from modules.keyboard_control import KeyboardControl
from modules.window_switcher import WindowSwitcher

from pynput.keyboard import Key

CODE_COUNT = 3
STOP_CODE = 90311024
HOST = "192.168.61.100"

tn = telnetlib.Telnet(HOST)

# setup
print(tn.read_until(b">"))
tn.write(b"dym=100\r\n")
print(tn.read_until(b">"))

tn.write(b"CA+\r\n")
print(tn.read_until(b">"))

pos = 0
last_rot = 0
count = 0

modules = {
    90311055: MelodyPlayer("harry_potter"),
    90311086: ScrollWheel(),
    93123457: KeyboardControl(Key.media_volume_down, Key.media_volume_up),
    12348: KeyboardControl('w', 's', time=.2),
    4210009: WindowSwitcher(timeout=.8)
}
module = modules[90311086]

while True:
    data = tn.read_until(b"\r\n").decode("ascii")
    code = int(data.split(" ")[-1])

    count+=1

    if count == 64:
        tn.write(b"CA-\r\n")
        tn.read_until(b">")
        tn.write(b"CA+\r\n")
        tn.read_until(b">")
        count = 0

    if code == STOP_CODE:
        break
    elif code in modules.keys():
        module = modules[code]
        print(f"module switched to {module.__class__.__name__}")
        continue

    new_rot = code % 10
    
    if new_rot != last_rot:
        diff = (new_rot - last_rot) % CODE_COUNT
        if diff > 1:
            diff *= -1
        if diff != 0:
            diff /= abs(diff)

        pos += diff

        module.update(diff)

        last_rot = new_rot

    print(f"count: {count}, pos: {pos}")

# turn laser off
tn.write(b"CA-\r\n")
tn.close()