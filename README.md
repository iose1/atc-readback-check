# atc-readback-check

A tiny, dependency-free Python checker for ATC read-backs, made for VATSIM & IVAO pilots.

It compares the numbers in a controller instruction with your read-back and tells you what you got wrong:
squawk, flight level / altitude, heading, speed, frequency, QNH and runway.

```
$ python readback_check.py "DLH4AB, descend flight level 110, squawk 2741" "Descend FL100, squawk 2741, DLH4AB"
level: expected 110, got 100
```

Spoken numbers work too ("one two four decimal seven two" → 124.72, "niner", "tree", "fife").

`rules.json` lists every item ICAO requires you to read back (Doc 4444 / Annex 10), handy for your own tools.

## Run the tests
```
python test_readback_check.py
```

## Limits
This only checks numbers, not full phraseology, order or callsigns. It's a learning aid, not a replacement for proper training.

## Want the full thing?
[SkyATC](https://skyatc.net) listens to your pilot client (vPilot, xPilot, swift, IVAO Altitude), shows the correct
read-back live, and includes a radio trainer with a speaking controller that works without a sim.
*(Disclosure: SkyATC is made by the same developer.)*

## License
MIT
