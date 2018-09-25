import subprocess

ret1 = subprocess.getoutput("date")
ret2 = subprocess.getoutput("date -u")
ret3 = subprocess.getoutput("date -u | wc")
ret4 = subprocess.check_output(["date", "-u"])
ret5 = subprocess.getstatusoutput("date")
ret6 = subprocess.call("date")
ret7 = subprocess.call("date -u", shell=True)
ret8 = subprocess.call(["date", "-u"])

rets = [ret1, ret2, ret3, ret4, ret5, ret6, ret7, ret8]

for ret in rets:
    print(ret)
