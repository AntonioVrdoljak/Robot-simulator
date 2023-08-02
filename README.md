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
