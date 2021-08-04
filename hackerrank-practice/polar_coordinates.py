import cmath

complex_cord = complex(input())

print(*cmath.polar(complex_cord), sep = '\n')
