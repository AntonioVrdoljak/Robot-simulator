import unittest
from app.robot import RobotSimulator


class TestRobot(unittest.TestCase):
    def test_valid_place_command(self):
        robot = RobotSimulator()
        robot.place(2, 3, 'NORTH')
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, 'NORTH')


if __name__ == '__main__':
    unittest.main()
