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


if __name__ == '__main__':
    unittest.main()
