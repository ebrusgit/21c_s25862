#TASK 8
from square_generator import SquareGenerator
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        cubes = [x**3 for x in range(start, end + 1)]
        return cubes

# Example usage:
cubic_gen = CubicGenerator()
start = 1
end = 5
cubes_list = cubic_gen.generate_squares(start, end)
print("Cubes:", cubes_list)


#TASK 9
from square_generator import SquareGenerator
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("Error: end cannot be less than the start")
        squares = [x**2 for x in range(start, end + 1)]
        return squares

cubic_gen = CubicGenerator()
start = 1
end = 5
try:
    squares_list = cubic_gen.generate_squares(start, end)
    print("Squares:", squares_list)
except ValueError as e:
    print(e)

#TASK 9 checker for the error
print("task 9 checker:")
start = 5
end = 1
try:
    squares_list = cubic_gen.generate_squares(start, end)
    print("Squares:", squares_list)
except ValueError as e:
    print(e)
