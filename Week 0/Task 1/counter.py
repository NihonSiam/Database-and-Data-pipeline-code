class Counter:
    def __init__(self):
        self.__count = 0  # count starts at 0

    def addCount(self):
        self.__count += 1  # increase count by 1

    def getCount(self):
        return self.__count  # return current count

    def zeroCount(self):
        self.__count = 0  # set count back to 0
