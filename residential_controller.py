# Column
class Column:
    def __init__(self, id, status, amountOfFloors, amountOfElevators):
        self.id = id
        self.status = status
        self.amountOfFloors = amountOfFloors
        self.amountOfElevators = amountOfElevators
        self.callButtonList = []
        self.elevatorList = []
         
        for number in range(self.amountOfFloors):
            buttonFloor = 1
            buttonID = 1 
            if buttonFloor < self.amountOfFloors:
                callButton = CallButton(buttonID, 'off', buttonFloor, 'up')
                self.callButtonList.append(callButton)
                buttonID += 1
            if buttonFloor > 1:
                callButton = CallButton(buttonID, 'off', buttonFloor, 'down')
                self.callButtonList.append(callButton)
                buttonID += 1
            buttonFloor += 1
            
        for number in range(self.amountOfElevators):
            elevatorID = 1
            elevator = Elevator(elevatorID, 'idle', self.amountOfFloors, 1)
            self.elevatorList.append(elevator)
            elevatorID += 1
            
    def requestElevator(self, requestedFloor, direction):
        elevator = self.findElevator(requestedFloor, direction)
        elevator.floorRequestList.append(requestedFloor)
        elevator.move()
        elevator.openDoors()
        return elevator
    
    def findElevator(self, requestedFloor, requestedDirection):
        elevatorInfo = {
            bestElevator: None,
            bestScore: 5,
            referenceGab: float('inf')
        }
        
 
 
 
        
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
        
        for number in range(self.amountOfFloors):
            floorNumber = 1
            floorRequestButtonID = 1
            floorButton = FloorRequestButton(floorRequestButtonID, 'off', floorNumber)
            self.floorRequestButtonList.append(floorButton)
            floorNumber += 1
            floorRequestButtonID += 1
    
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
            self.floorRequestList.pop(0)
        
    def sortFloorRequestList(self):
        if self.direction == 'up':
            self.floorRequestList.sort()
        else:
            self.floorRequestList.sort(reverse=True)
            
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

# testColumn = Column(1, 'online', 10, 2)            
# print(len(testColumn.callButtonList))
# print(testColumn.callButtonList[0].status)
# print(len(testColumn.elevatorList))
# print(testColumn.elevatorList)
# print(testColumn.__dict__)

# testElevator = Elevator(1, 'lol', 5, 1)
# testElevator.floorRequestList = [10, 4, 22, 15]
# testElevator.direction = 'up'
# testElevator.sortFloorRequestList()
# print(testElevator.floorRequestList)

# l = [10, 2, 28, 15]
# l.sort(reverse=True)
# print(l)