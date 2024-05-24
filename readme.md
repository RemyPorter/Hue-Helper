# Hue Helper
A simple CLI wrapper around the Phue library so we can easily link it to QLab.

I originally wrote this to support **The Secret Hour** at [Ensemble Actor's Studio](https://www.ensembleactors.com/theater-co).

## Installing
`pip install phue`

## Running from the Shell
```
usage: python3 hue.py [-h] --ip IP [--hue HUE] [--sat SAT] [--bri BRI] [--transition TRANSITION] [--on]
                               [--off]
                               light_id [light_id ...]
```

## Running from QLab

Add a script cue, and fill the body thusly:

```
do shell script "/path/to/python/python3 '/path/to/hue/helper/hue.py' --ip 192.168.1.22 --bri 255 --transition 0.5 --on 1 2 3 4"
```

NB: use an absolute path to the Python version you want to use- AppleScript defaults to the system Python. If you've installed a version from Homebrew or PyEnv or whatever, AppleScript won't use it.

## Notes
Setting brightness to zero doesn't always work on Hue bulbs, so if you want the light off, you must *also* set the light to `--off`. The `--off` won't fire until the end of the transition.