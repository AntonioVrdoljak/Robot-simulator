# Robot Simulator

## Description

The Robot Simulator is a Python application that simulates a toy robot moving on a square tabletop. 
The tabletop has dimensions of 5 units x 5 units, and the robot can be placed on it in various positions and orientations (North, South, East, West). 
The simulator allows you to control the robot's movements and receive its position and orientation.

## Features

- PLACE will put the toy robot on the table in position `X`,`Y` and facing `NORTH`, `SOUTH`, `EAST` or
`WEST`.
- The origin (0,0) can be considered to be the `SOUTH WEST` most corner.
- The first valid command to the robot is a `PLACE` command, after that, any sequence of
commands may be issued, in any order, including another `PLACE` command. The application
should discard all commands in the sequence until a valid `PLACE` command has been
executed.
- `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
- `LEFT` and `RIGHT` will rotate the robot 90 degrees in the specified direction without changing
the position of the robot.
- `REPORT` will announce the `x`,`y` and `facing` of the robot. 
- A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands

### Constraints:
The toy robot must not fall off the table during movement. This also includes the initial
placement of the toy robot.
Any move that would cause the robot to fall must be ignored.

## Getting Started

To get started with the Robot Simulator, follow these steps:

1. Clone the repository to your local machine (ex. SSH):
```
git clone git@github.com:AntonioVrdoljak/Robot-simulator.git
cd Robot-simulator
```
2. Install Python (if you don't have it already)
3. (Optional) Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
```

## Usage

To use the Robot Simulator, run the main.py script:

1. Open the Command Line or Terminal
2. Navigate to the Directory:
```
C:/Users/UserName/Documents/Projects/Robot-simulator/app/
```
3. To use the Robot Simulator, run the robot.py script:
```
python robot.py
```

### Commands

The following commands are available for interacting with the robot:

- `PLACE X,Y,F` Place the robot at position X,Y with orientation F (NORTH, EAST, SOUTH, or WEST).
- `MOVE` Move the robot one unit forward in the direction it's facing.
- `LEFT` Rotate the robot 90 degrees to the left.
- `RIGHT` Rotate the robot 90 degrees to the right.
- `REPORT` View the current position and orientation of the robot.
- `EXIT` Exit the simulator.
  
The first valid command must be a PLACE command. After that, any sequence of commands can be issued, including another PLACE command.


## Tests
The Robot Simulator includes a test suite to ensure the correct functionality of its components. 
To run the tests, execute the following command,but first make sure you're in the root directory of the project:
```
python -m unittest discover tests
```
The test suite uses Python's built-in unittest framework and can be found in the tests directory.
It covers various scenarios to validate the correctness of the simulator's behavior.
