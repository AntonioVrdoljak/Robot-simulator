class RobotSimulator:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.valid_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.placed = False

    def place(self, x, y, direction):
        if direction.upper() in self.valid_directions:
            self.x = x
            self.y = y
            self.direction = direction.upper()
            self.placed = True

    def report(self):
        print(f"Output: {self.x},{self.y},{self.direction}")


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


if __name__ == "__main__":
    main()
