# Exercise 3.5
# I'm sure there are more efficient ways, but I did this myself :)  -- Not sure how to remove the words "None" that appear after the column_4times(column) function is used.

# row:   +----+----+
half_row = ('+' + ('-' * 4))
row = half_row * 2

# bar lines:    |    |    |     (repeated for 4 lines)
def column_4times(column):
    print(column)
    print(column)
    print(column)
    print(column)  
    
half_column = ('|' + ' ' * 4)
column = (half_column * 2 + '|')

print(row + '+')
print(column_4times(column))
print(row + '+')
print(column_4times(column))
print(row + '+')


# Write a function that draws a similar grid with four rows and four columns.

def do_twice(f,r,c):
    f(r,c)
    f(r,c)
    
def print_twice(row, column):
    print(row)
    print(column)
    print(column)
    print(column)
    print(column)
    
def do_four(f,r,c):
    do_twice(f,r,c)
    do_twice(f,r,c)

do_four(print_twice, '+----+----+', '|    |    |')
print('+----+----+')




