# Python Controller

### Python is a really fun language!

At last the Python script if done and working! This was a fun project to complete!
If you want to test it, call one of the scenarios at the bottom and run the code on your terminal!
Scenario1() , Scenario2() , Scenario3()
```C#
def Scenario1():
    # Setting the base values for this scenario
    column.elevatorList[0].currentFloor = 2
    column.elevatorList[1].currentFloor = 6
    print('User is on floor 3 and wants to go up to floor 7')
    elevator = column.requestElevator(3, 'up')
    print('Elevator A is sent to floor:', column.elevatorList[0].currentFloor)
    print('User enters the elevator and presses of floor 7')
    elevator.requestFloor(7)
    print('...')
    print('User reaches floor', column.elevatorList[0].currentFloor, 'and gets out')

Scenario1()
```
Now on to the next challenge!