mousetrap.py
by John Shaffstall

Example:

#!/usr/bin/env python
import MouseTrap

# capture mouse positions
mouseTrap = MouseTrap.MouseTrap()
mouseTrap.open()

# read mouse positions
positions = mouseTrap.getPositions()

# ...do something with the positions...

# capture mouse again
mouseTrap.open()

# read mouse positions again
positions = mouseTrap.getPositions()

# ...do something else with the positions...

# all done! :)
