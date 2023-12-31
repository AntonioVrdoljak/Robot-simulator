import unittest
from app.robot import RobotSimulator


class TestRobot(unittest.TestCase):
    def test_valid_place_command(self):
        robot = RobotSimulator()
        robot.place(2, 3, 'NORTH')
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, 'NORTH')

    def test_invalid_place_command(self):
        robot = RobotSimulator()
        robot.place(5, 2, 'NORTH')  # Invalid position
        self.assertFalse(robot.x is not None and robot.y is not None and robot.direction is not None)

        robot.place(2, 3, 'INVALID')  # Invalid direction
        self.assertFalse(robot.x is not None and robot.y is not None and robot.direction is not None)

    def test_move_command(self):
        robot = RobotSimulator()
        robot.place(2, 2, 'NORTH')
        robot.move()
        self.assertEqual(robot.y, 3)
        robot.left()
        robot.move()
        self.assertEqual(robot.x, 1)
        robot.right()
        robot.move()
        self.assertEqual(robot.x, 1)

    def test_left_right_commands(self):
        robot = RobotSimulator()
        robot.place(2, 2, 'NORTH')
        robot.left()
        self.assertEqual(robot.direction, 'WEST')
        robot.right()
        self.assertEqual(robot.direction, 'NORTH')
        robot.right()
        self.assertEqual(robot.direction, 'EAST')

    def test_report_command(self):
        robot = RobotSimulator()
        robot.place(2, 2, 'NORTH')
        with self.assertLogs() as log:
            robot.report()
        self.assertIn("INFO:root:Output: 2,2,NORTH", log.output[0])

    def test_ignore_commands_before_place(self):
        robot = RobotSimulator()
        commands = ['MOVE', 'LEFT', 'RIGHT', 'REPORT', 'PLACE 2,2,NORTH', 'REPORT']

        for command in commands:
            if command.startswith('PLACE'):
                _, args = command.split(' ', 1)
                x, y, direction = args.split(',')
                robot.place(int(x), int(y), direction)
            elif robot.placed:
                if command == 'MOVE':
                    robot.move()
                elif command == 'LEFT':
                    robot.left()
                elif command == 'RIGHT':
                    robot.right()
                elif command == 'REPORT':
                    with self.assertLogs() as log:
                        robot.report()
                    self.assertIn("INFO:root:Output: 2,2,NORTH", log.output[0])
            else:
                self.assertFalse(robot.x is not None and robot.y is not None and robot.direction is not None)


if __name__ == '__main__':
    unittest.main()
