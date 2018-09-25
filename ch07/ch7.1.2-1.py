#!/usr/local/bin/python3

print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)
print('%d%%' % 100)

actor = 'Richar Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

n = 42
f = 7.03
s = 'string cheese'
print('%s %f %s' % (n, f, s))
print('%10d %10f %10s' % (n, f, s))
print('%-10d %-10f %-10s' % (n, f, s))
print('%10.4d %10.4f %10.4s' % (n, f, s))
print('%.4d %.4f %.4s' % (n, f, s))
print('%*.*d %*.*f %*.*s' % (10, 4,  n, 10, 4, f, 10, 4, s))

print('{} {} {}' .format(n, f, s))
print('{2} {0} {1}' .format(f, s, n))
print('{n} {f} {s}' .format(n=42, f=7.03, s='string cheese'))

d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}' .format(d, 'other'))

print('{0:d} {1:f} {2:s}' .format(n, f, s))
print('{n:d} {f:f} {s:s}' .format(n=42, f=7.03, s='string cheese'))
print('{0:10d} {1:10f} {2:10s}' .format(n, f, s))
print('{0:>10d} {1:>10f} {2:>10s}' .format(n, f, s))
print('{0:<10d} {1:<10f} {2:<10s}' .format(n, f, s))
print('{0:^10d} {1:^10f} {2:^10s}' .format(n, f, s))
print('{0:>10d} {1:>10.4f} {2:>10.4s}' .format(n, f, s))
print('{0:!^20s}' .format('BIG SALE'))
