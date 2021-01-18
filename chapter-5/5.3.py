Def is_triangle(a, b, c):
       if a<=b+c and b<=a+c and c<=a+b:
           return 'yes'
       else:
           return 'no'

is_triangle(1, 12, 3)
'no'