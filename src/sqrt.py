
# import stdio
import sys

# Accept float c as a command-line argument. Write to standard
# output the square root of c to 15 decimal places of accuracy.
# Use Newton's method.

EPSILON = 1e-15

if len(sys.argv)==1:
    c = 1e33
else:
    c = float(sys.argv[1])
t = c
while abs(t - c/t) > (EPSILON):
    # Replace t by the average of t and c/t.
    t = (c/t + t) / 2.0
print(t)

