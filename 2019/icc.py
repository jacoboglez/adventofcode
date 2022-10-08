''' Intcode Computer impolementation. 
From: https://github.com/m-berk/AdventOfCode2019/blob/master/Day9.2.py '''

class intCodeComputer:
    def __init__(self, programCode, id=0, relBase=0, indx=0, emptySpace=10000, inptArr=[], verbose=False):
        self.relativeBase = 0
        self.memory = []
        self.memory = programCode.copy()
        for i in range(emptySpace):
            self.memory.append(0)
        self.index = indx
        self.inputArray = inptArr.copy()
        self.outputArray = []
        self.id = id
        self.finished = False
        self.verbose = verbose


    def setSingleMemoryAddress(self, pos, val):
        self.memory[pos] = val


    def compute(self):  # computes until there's an input requiered

        while (not self.finished):

            # formatting OPCODE

            TempLen = len(str(self.memory[self.index]))
            StringToAdd = ""
            for i in range(5 - TempLen):
                StringToAdd += "0"
            self.memory[self.index] = StringToAdd + str(self.memory[self.index])
            # print(self.memory[self.index])

            # reading parameters according to the given parameter modes ----------------------
            parameters = []
            parameterMode = str(self.memory[self.index][:3])
            # print(self.memory[self.index], parameterMode)
            # print(parameterMode)
            OpCode = str(self.memory[self.index])[-2:]
            self.memory[self.index] = int(self.memory[self.index])
            if (parameterMode[2] == "0"):
                parameters.append(int(self.memory[self.index + 1]))
            elif (parameterMode[2] == "1"):
                parameters.append(self.index + 1)
            else:  # paramMode 2
                parameters.append(int(self.memory[self.index + 1]) + self.relativeBase)

            if (parameterMode[1] == "0"):
                parameters.append(int(self.memory[self.index + 2]))
            elif (parameterMode[1] == "1"):
                parameters.append(self.index + 2)
            else:  # paramMode 2
                parameters.append(self.memory[self.index + 2] + self.relativeBase)

            if (parameterMode[0] == "0"):
                parameters.append(int(self.memory[self.index + 3]))
            elif (parameterMode[0] == "1"):
                parameters.append(self.index + 3)
            else:  # paramMode 2
                parameters.append(int(self.memory[self.index + 3]) + self.relativeBase)
            

            if (OpCode == "01"):
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) + int(self.memory[parameters[1]])
                self.index += 4
            elif (OpCode == "02"):
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) * int(self.memory[parameters[1]])
                self.index += 4
            elif (OpCode == "03"):
                if (len(self.inputArray) != 0):
                    self.memory[parameters[0]] = self.inputArray[0]
                    self.index += 2
                    self.inputArray.pop(0)
                else:
                    if self.verbose: print("waiting input")
                    break
            elif (OpCode == "04"):
                # print("output from int comp "+str(self.id)+ "  :" +str(self.memory[parameters[0]]))
                self.outputArray.append(self.memory[parameters[0]])
                self.index += 2
            elif (OpCode == "05"):
                if (self.memory[parameters[0]] != 0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif (OpCode == "06"):
                if (self.memory[parameters[0]] == 0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif (OpCode == "07"):
                if (int(self.memory[parameters[0]]) < int(self.memory[parameters[1]])):
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif (OpCode == "08"):
                if (self.memory[parameters[0]] == self.memory[parameters[1]]):
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif (OpCode == "09"):
                self.relativeBase += self.memory[parameters[0]]
                self.index += 2
            elif (OpCode == "99"):
                if self.verbose: print(str(self.id) + ". computer has finished")
                self.finished = True
                break


    def addInput(self, input):
        self.inputArray.append(input)

    def printOutputs(self):
        print(self.outputArray)

    def getOutput(self):
        return self.outputArray

    def flushOutputs(self):
        self.outputArray.clear()

