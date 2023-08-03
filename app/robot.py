class RobotSimulator:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.valid_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.placed = False

    def place(self, x, y, direction):
        if self.is_valid_position(x, y) and direction.upper() in self.valid_directions:
            self.x = x
            self.y = y
            self.direction = direction.upper()
            self.placed = True

    def report(self):
        print(f"Output: {self.x},{self.y},{self.direction}")

    def move(self):
        if self.direction == 'NORTH':
            self.y = min(4, self.y + 1)
        elif self.direction == 'SOUTH':
            self.y = max(0, self.y - 1)
        elif self.direction == 'EAST':
            self.x = min(4, self.x + 1)
        elif self.direction == 'WEST':
            self.x = max(0, self.x - 1)

    def left(self):
        current_index = self.valid_directions.index(self.direction)
        new_index = (current_index - 1) % 4
        self.direction = self.valid_directions[new_index]

    def right(self):
        current_index = self.valid_directions.index(self.direction)
        new_index = (current_index + 1) % 4
        self.direction = self.valid_directions[new_index]

    @staticmethod
    def is_valid_position(x, y):
        return 0 <= x <= 4 and 0 <= y <= 4


def main():
    command_place = 'PLACE'
    robot = RobotSimulator()

    while True:
        commands = input("Enter commands (PLACE X,Y,F MOVE LEFT RIGHT REPORT or EXIT ").strip().upper().split()

        if not commands:
            print("Incorrect input, please try again.")
            continue

        for command in commands:
            if command == 'EXIT':
                print("Exiting the robot simulator.")
                return
            elif command.startswith(command_place):
                place_index = commands.index(command)
                additional_place_command = commands[place_index + 1]
                command = command + ' ' + additional_place_command
                _, args = command.split()
                x, y, direction = args.split(',')
                robot.place(int(x), int(y), direction)
            elif robot.placed:
                if command == 'REPORT':
                    robot.report()
                elif command == 'MOVE':
                    robot.move()
                elif command == 'LEFT':
                    robot.left()
                elif command == 'RIGHT':
                    robot.right()
            else:
                print("Robot has not been placed yet. Please use the PLACE command to place the robot.")


if __name__ == "__main__":
    main()
