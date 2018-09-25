# linux only

import os

uid = 5
gid = 22
os.chown("oops", uid, gid)
