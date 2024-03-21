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
