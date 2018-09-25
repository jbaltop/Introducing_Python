import os

os.chmod("oops.txt", 0o400)

import stat

os.chmod("oops.txt", stat.S_IRUSR)
