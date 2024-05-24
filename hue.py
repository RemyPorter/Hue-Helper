from phue import Bridge
import argparse

parser = argparse.ArgumentParser(
    prog="Phillips Hue Controller",
    description="Control Hue bulbs via the CLI"
)
parser.add_argument("light_id", type=int, nargs="+", help="The light IDs we want to operate on")
parser.add_argument("--ip", type=str, help="The IP of the bridge", required=True)
parser.add_argument("--hue", type=int, help="The hue to set them to (0-65535)", required=False)
parser.add_argument("--sat", type=int, help="The saturation to set them to (0-255)", required=False)
parser.add_argument("--bri", type=int, help="The brightenss to set them to (0-255)", required=False)
parser.add_argument("--transition", type=float, help="The transition time in seconds", default=0, required=False)
parser.add_argument("--on", dest="on", help="Turn the fixture on", action="store_const", const=True)
parser.add_argument("--off", dest="on", help="Turn the fixture on", action="store_const", const=False)

def main():
    args = parser.parse_args()
    b = Bridge(args.ip)
    command = {
        "transitiontime": int(args.transition * 10.0),
        "on": args.on
    }
    if (args.hue is not None): 
        command["hue"] = args.hue
    if (args.sat is not None): 
        command["sat"] = args.sat
    if (args.bri is not None): 
        command["bri"] = args.bri
    print(command)
    b.set_light(args.light_id[0], command)

main()
    
