class RobotSimulator:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.valid_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.placed = False


def main():
    robot = RobotSimulator()

    while True:
        commands = input("Enter commands (PLACE X,Y,F MOVE LEFT RIGHT REPORT or EXIT ").strip().upper().split()

        if not commands:
            print("Incorrect input, please try again")
            continue

        for command in commands:
            if command == 'EXIT':
                print("Exiting the toy robot simulator.")
                return


if __name__ == "__main__":
    main()
