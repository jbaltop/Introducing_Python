# windows에는 chown이 없음

import os

uid = 5
gid = 22
os.chown('oops', uid, gid)
