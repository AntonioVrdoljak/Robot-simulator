class RobotSimulator:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.valid_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.placed = False


def main():
    robot = RobotSimulator()


if __name__ == "__main__":
    main()
