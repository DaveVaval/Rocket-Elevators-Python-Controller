# Column
class Column:
    def __init__(self, id, status, amountOfFloors, amountOfElevators):
        self.id = id
        self.status = status
        self.amountOfFloors = amountOfFloors
        self.amountOfElevators = amountOfElevators
        self.callButtonList = []
        self.elevatorList = []
        buttonFloor = 1
        buttonID = 1 
         # On initiation the column will create it's call buttons
        for number in range(self.amountOfFloors):
            if buttonFloor < self.amountOfFloors:
                callButton = CallButton(buttonID, 'off', buttonFloor, 'up')
                self.callButtonList.append(callButton)
                buttonID += 1
            if buttonFloor > 1:
                callButton = CallButton(buttonID, 'off', buttonFloor, 'down')
                self.callButtonList.append(callButton)
                buttonID += 1
            buttonFloor += 1
        # On initiation the column will create it's elevators    
        elevatorID = 1
        for number in range(self.amountOfElevators):
            elevator = Elevator(elevatorID, 'idle', self.amountOfFloors, 1)
            self.elevatorList.append(elevator)
            elevatorID += 1
     # This method will be called whenever a user requests an elevator       
    def requestElevator(self, requestedFloor, direction):
        elevator = self.findElevator(requestedFloor, direction)
        elevator.floorRequestList.append(requestedFloor)
        elevator.move()
        elevator.openDoors()
        return elevator
    # Finding the best elevator is managed by this method
    def findElevator(self, requestedFloor, requestedDirection):
        elevatorInfo = {
            "bestElevator": None,
            "bestScore": 5,
            "referenceGap": float('inf')
        }
        for elevator in self.elevatorList:
            if requestedFloor == elevator.currentFloor and elevator.status == 'idle' and requestedDirection == elevator.direction:
                elevatorInfo = self.checkElevator(1, elevator, elevatorInfo, requestedFloor)
            elif requestedFloor > elevator.currentFloor and elevator.direction == 'up' and requestedDirection == elevator.direction:
                elevatorInfo = self.checkElevator(2, elevator, elevatorInfo, requestedFloor)
            elif requestedFloor < elevator.currentFloor and elevator.direction == 'down' and requestedDirection == elevator.direction:
                elevatorInfo = self.checkElevator(2, elevator, elevatorInfo, requestedFloor)
            elif elevator.status == 'idle':
                elevatorInfo = self.checkElevator(3, elevator, elevatorInfo, requestedFloor)
            else:
                elevatorInfo = self.checkElevator(4, elevator, elevatorInfo, requestedFloor)
        return elevatorInfo["bestElevator"]
    
    def checkElevator(self, baseScore, elevator, elevatorInfo, floor):
        if baseScore < elevatorInfo["bestScore"]:
            elevatorInfo["bestScore"] = baseScore
            elevatorInfo["bestElevator"] = elevator
            elevatorInfo["referenceGap"] = abs(elevator.currentFloor - floor)
        elif elevatorInfo["bestScore"] == baseScore:
            gap = abs(elevator.currentFloor - floor)
            if elevatorInfo["referenceGap"] > gap:
                elevatorInfo["bestScore"] = baseScore
                elevatorInfo["bestElevator"] = elevator
                elevatorInfo["referenceGap"] = gap
        return elevatorInfo
 
        
# Elevator
class Elevator:
    def __init__(self, id, status, amountOfFloors, currentFloor):
        self.id = id
        self.status = status
        self.amountOfFloors = amountOfFloors
        self.currentFloor = currentFloor
        self.direction = None
        self.door = Doors(id, 'closed')
        self.floorRequestButtonList = []
        self.floorRequestList = []
        # On initiation the elevator will create it's own buttons
        for number in range(self.amountOfFloors):
            floorNumber = 1
            floorRequestButtonID = 1
            floorButton = FloorRequestButton(floorRequestButtonID, 'off', floorNumber)
            self.floorRequestButtonList.append(floorButton)
            floorNumber += 1
            floorRequestButtonID += 1
    # This method will push the requested floor to the request list
    # and calls the elevator to move and open it's doors 
    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.sortFloorRequestList()
        self.move()
        self.openDoors()
            
    def move(self):
        while len(self.floorRequestList) != 0:
            destination = self.floorRequestList[0]
            self.status = 'moving'
            if self.currentFloor < destination:
                self.direction = 'up'
                while self.currentFloor < destination:
                    self.currentFloor += 1
            elif self.currentFloor > destination:
                self.direction = 'down'
                while self.currentFloor > destination:
                    self.currentFloor -= 1
            self.status = 'idle'
            self.floorRequestList.pop(0) # Once the floor is reached it will delete the floor from the request List
        
    def sortFloorRequestList(self):
        if self.direction == 'up':
            self.floorRequestList.sort() # This will sort the request list ascending
        else:
            self.floorRequestList.sort(reverse=True) # This will sort the request list descending
            
    def openDoors(self):
        self.door.status = 'open'
        self.door.status = 'closed'
            
# Call Button
class CallButton:
    def __init__(self, id, status, floor, direction):
        self.id = id
        self.status = status
        self.floor = floor
        self.direction = direction

# Floor Request Button
class FloorRequestButton:
    def __init__(self, id, status, floor):
        self.id = id
        self.status = status
        self.floor = floor

# Doors
class Doors:
    def __init__(self, id, status):
        self.id = id
        self.status = status
        
        
        
#----------------------------------------------------------------// Testing //--------------------------------------------------------------------------
# Creating an instance of Column
column = Column(1, 'online', 10, 2)

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
    
def Scenario2():
    # Setting the base values for this Scenario
    column.elevatorList[0].currentFloor = 10
    column.elevatorList[1].currentFloor = 3
    print('User is on floor 1 and wants to go up to floor 6')
    elevator = column.requestElevator(6, 'up')
    print('Elevator B is sent to floor:', column.elevatorList[1].currentFloor)
    print('User enters the elevator and presses of floor 6')
    elevator.requestFloor(6)
    print('...')
    print('User reaches floor', column.elevatorList[1].currentFloor, 'and gets out')
    print()
    print('2 minutes later...')
    print()
    print('Another user is on floor 3 and wants to go up to floor 5')
    elevator = column.requestElevator(5, 'up')
    print('Elevator B is sent to floor:', column.elevatorList[1].currentFloor)
    print('User enters the elevator and presses of floor 5')
    elevator.requestFloor(5)
    print('...')
    print('User reaches floor', column.elevatorList[1].currentFloor, 'and gets out')
    print()
    print('Some time after...')
    print()
    print('Another user is on floor 9 and wants to go up to floor 2')
    elevator = column.requestElevator(9, 'down')
    print('Elevator A is sent to floor:', column.elevatorList[0].currentFloor)
    print('User enters the elevator and presses of floor 2')
    elevator.requestFloor(2)
    print('...')
    print('User reaches floor', column.elevatorList[0].currentFloor, 'and gets out')
    
def Scenario3():
    # Setting the base values for this Scenario
    column.elevatorList[0].currentFloor = 10
    column.elevatorList[0].direction = 'down'
    column.elevatorList[1].currentFloor = 3
    print('User is on floor 3 and wants to go up to floor 2')
    print('Elevator A is on floor 10 and Elevator B is currently moving from floor 3 to 6')
    column.elevatorList[1].requestFloor(6)
    elevator = column.requestElevator(3, 'down')
    print('Elevator A is sent to floor:', column.elevatorList[0].currentFloor)
    print('User enters the elevator and presses of floor 2')
    elevator.requestFloor(2)
    print('...')
    print('User reaches floor', column.elevatorList[0].currentFloor, 'and gets out')
    print()
    print('5 minutes later...')
    print()
    print('Another user is on floor 10 and wants to go up to floor 3')
    elevator = column.requestElevator(10, 'down')
    print('Elevator B is sent to floor:', column.elevatorList[1].currentFloor)
    print('User enters the elevator and presses of floor 2')
    elevator.requestFloor(2)
    print('...')
    print('User reaches floor', column.elevatorList[1].currentFloor, 'and gets out')