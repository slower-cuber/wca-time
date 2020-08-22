# wca-time
time of all events of each contestant in each competition in recent 2 years

## event numbers
```
3x3x3 Cube : 105628
2x2x2 Cube : 72853
Pyraminx : 52527
4x4x4 Cube : 47264
3x3x3 One-Handed : 38211
Skewb : 35095
5x5x5 Cube : 25882
Megaminx : 18110
Square-1 : 14635
6x6x6 Cube : 11409
7x7x7 Cube : 9319
3x3x3 Blindfolded : 9057
Clock : 8715
3x3x3 Fewest Moves : 6742
3x3x3 With Feet : 3285
4x4x4 Blindfolded : 1224
5x5x5 Blindfolded : 576
```

## Code
```
$ pip install -r requirements.txt

# $0 <event x> <event y> , notice the quotes
$ python plot_events.py "3x3x3 Cube" "5x5x5 Cube"
```

### valid event
```
VALID_EVENTS = [
    '2x2x2 Cube', '3x3x3 Blindfolded', '3x3x3 Cube', '3x3x3 Fewest Moves', '3x3x3 One-Handed',
    '3x3x3 With Feet', '4x4x4 Blindfolded', '4x4x4 Cube', '5x5x5 Blindfolded', '5x5x5 Cube',
    '6x6x6 Cube', '7x7x7 Cube', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1',
]
```

