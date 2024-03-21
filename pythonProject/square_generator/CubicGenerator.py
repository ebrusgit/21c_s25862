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
