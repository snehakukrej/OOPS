'''
    def show(self):
        if len(self.owes) > 0:
            for i in self.owes:
                print(self.name+" owes "+i+": "+str(self.owes[i]))
        if len(self.gets) > 0:
            for i in self.gets:
                print(i+" owes "+self.name+": "+str(self.gets[i]))
        if (len(self.gets) == 0) and (len(self.owes) == 0):
            print("No balances")
'''
from user import user
from typing import List
def main():
    p = ProcessInput()
    while True:
        #process each line in input
        inputList = input().strip().split(' ')
        if inputList[0] == 'ADD':
            p.processAdd(inputList)
        if inputList[0] == 'EXPENSE':
            p.processExpense(inputList)
        if inputList[0] == 'SHOW':
            p.processShow(inputList)
        if inputList[0] == '':
            exit(0)
        

class ProcessInput:
    def __init__(self):
        self.users = dict()
        self.owes = dict()

    # process 'ADD' function
    def processAdd(self,inputList : List[str]):
        usersString = inputList[2:]
        count = 1
        for usr in usersString:
            id = 'u'+str(count)
            self.users[id] = user(id,usr)
            count += 1
    
    #process 'EXPENSE' function
    def processExpense(self, inputList: List[str]):
        owedTo = inputList[1]
        amount = int(inputList[2])
        num = int(inputList[3])
        owedBy = inputList[4:4+num]

        # Update the transaction 
        def updateAmount(owedTo, usr, amt) :
            if owedTo == usr : return
            if (owedTo,usr) in self.owes:
                self.owes[(owedTo,usr)] += amt
            elif (usr,owedTo) in self.owes:
                self.owes[(usr,owedTo)] -= amt
            else:
                self.owes[(owedTo,usr)] = amt


        if "EQUAL" in inputList:
            amount = round(amount / num, 2)
            for usr in owedBy:
                updateAmount(owedTo,usr,amount)


        if "EXACT" in inputList:
            amountList = map(int,inputList[5+num:])
            for usr,amt in zip(owedBy,amountList):
                updateAmount(owedTo, usr, amt)

        if "PERCENT" in inputList:
            amountList = map(int,inputList[5+num:])
            amountList = map(lambda x: round((x/100)*amount, 2), amountList)
            for usr,amt in zip(owedBy, amountList):
                updateAmount(owedTo, usr, amt)
    
    #process 'SHOW' function
    def processShow(self, inputList: List[str]):

        def printLine(pair):
            if self.owes[pair] < 0:
                print(self.users[pair[0]].name+" owes "+ self.users[pair[1]].name+": "+ str(-(self.owes[pair])))
            if self.owes[pair] > 0:
                print(self.users[pair[1]].name+" owes "+ self.users[pair[0]].name+ ": "+ str(self.owes[pair]))

        if len(self.owes.keys()) == 0:
            print("No balances")
        if len(inputList) == 1:
            for pair in self.owes:
                printLine(pair)
        else :
            count = 0
            for pair in self.owes:
                if inputList[1] in pair:
                    count += 1
                    printLine(pair)
            if count ==0: print("No balances")



if __name__ == '__main__':
    main()