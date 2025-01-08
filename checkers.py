x1  = int(input("enter x 1 coordinates: "))
y1 = int(input("enter y 1 coordinates: "))
# Coordinates of the second square
x2 = int(input("enter x 2 coordinates: "))
y2 = int(input("enter y 2 coordinates: "))
# Check if the king can move from the first square to the second in one move
can_move = -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1

print(int(can_move),"if the result is 0 the king can't move, if the result is 1 the king can move")
# Output: 1 if the king can move, otherwise 0
