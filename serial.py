class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """ initiate a serial generator with a passed in start value """
        self.start = start
        self.count = -1
    
    def generate(self):
        """ generates the next sequential number """
        self.count += 1
        return self.start + self.count

    def reset(self):
        """ resets the serial generator to the original start value """
        self.count = -1