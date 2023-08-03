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


if __name__ == '__main__':
    unittest.main()
