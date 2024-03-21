#TASK 1
squares = [x**2 for x in range(1, 11)]
print(squares)

#TASK 2
def generate_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares

start = 1
end = 10
squares_list = generate_squares(start, end)
print(squares_list)


#TASK 3
class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x**2 for x in range(start, end + 1)]
        return squares

square_gen = SquareGenerator()
start = 1
end = 10
squares_list = square_gen.generate_squares(start, end)
print(squares_list)

#TASK 4
import math
class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x**2 for x in range(start, end + 1)]
        square_roots = [int(math.sqrt(num)) if math.sqrt(num).is_integer() else math.sqrt(num) for num in squares]
        return square_roots

square_gen = SquareGenerator()
start = 1
end = 10
square_roots_list = square_gen.generate_squares(start, end)
print(square_roots_list)

#TASK 5
import math

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("Error: end cannot be less than the start")
        squares = [x**2 for x in range(start, end + 1)]
        square_roots = [int(math.sqrt(num)) if math.sqrt(num).is_integer() else math.sqrt(num) for num in squares]
        return square_roots

square_gen = SquareGenerator()
start = 1
end = 10
square_roots_list = square_gen.generate_squares(start, end)
print(square_roots_list)

start = 10
end = 1
try:
    square_roots_list = square_gen.generate_squares(start, end)
    print(square_roots_list)
except ValueError as e:
    print(e)
