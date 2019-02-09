import can

can_bus = can.interface.Bus('can0', bustype='socketcan',bitrate=1000)


