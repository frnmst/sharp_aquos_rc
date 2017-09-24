# sharp_aquos_rc

Control Sharp Aquos SmartTVs with Python

## Quick start

Before installing this API, follow the instructions reported at
https://sharp-aquos-remote-control.github.io/index.html#quick-start

## Installation and basic instructions

Installation via pip:

    pip install sharp_aquos_rc

### Command profiles

Depending on the country of purchase of the television you must choose between
one of the available profiles or command maps (see 
the `./sharp_aquos_rc/commands` directory):

- cn
- eu
- jp
- us

The `us` profile is used by default, so to choose another one simply pass it 
as an option to the class constructor. For example:

    >>> tv = sharp_aquos_rc.TV('192.168.1.5', 10002, 'admin', 'password', command_map='eu')


### Examples

    >>> import sharp_aquos_rc
    >>>
    >>> tv = sharp_aquos_rc.TV('192.168.1.5', 10002, 'admin', 'password')
    >>>
    >>> tv.power() # Returns 1 if TV is on and 0 if TV is off
    1
    >>> tv.power(0) # Turn the TV off
    True
    >>> tv.input('HDMI 2') # Set the TV to HDMI Input 2
    True

## Documentation

Full Documentation is available through pydoc

    pydoc sharp_aquos_rc

## TODO/Contribute

Contributions and Pull Requests always welcome.

Currently on the TODO list:
- Unit Tests
- Error Checking and Input Validation
- Better timeouts for sequential operations so that the sent 
  commands don't get ignored.
- Documentation.

## LICENSE

MIT

