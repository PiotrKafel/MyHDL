from myhdl import block

SLOW, MEDIUM, FAST = range(3)

@block
def top(dots = ..., speed=SLOW):
    dots
    def slowAndSmall():
       dots
    dots
    def fastAndLarge():
       dots
    if speed == SLOW:
        return slowAndSmall()
    elif speed == FAST:
        return fastAndLarge()
    else:
        raise NotImplementedError