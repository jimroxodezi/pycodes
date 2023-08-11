

import os
import fcntl

# eject request code in linux
EJECT = 0X5309

fd = os.open("/dev/cdrom", os.O_RDONLY | os.O_NONBLOCK)
# perform the eject request on the file descriptor
fcntl.ioctl(fd, EJECT, 0)
os.close(fd)