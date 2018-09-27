# p208

n = 42
f = 7.03
s = "string cheese"

print("%s %f %s" % (n, f, s))
print("%10d %10f %10s" % (n, f, s))
print("%-10d %-10f %-10s" % (n, f, s))
print("%10.4d %10.4f %10.4s" % (n, f, s))
print("%.4d %.4f %.4s" % (n, f, s))
print("%*.*d %*.*f %*.*s" % (10, 4, n, 10, 4, f, 10, 4, s))
