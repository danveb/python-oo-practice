"""Python serial number generator."""

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
    # dunder init method (constructor); self and start=0 as param
    def __init__(self, start=0):
        """Create a starting number to count from and a counter to keep track of # times called"""
        self.start = self.current_num = start 
        self.count = -1 
    
    # instance method -> generate() 
    def generate(self):
        """return starting number first time called and increment # after"""
        self.count += 1 
        if self.count == 0:
            return self.current_num 
        else:
            self.current_num += 1 
            return self.current_num
    
    # instance method -> reset() 
    def reset(self):
        """reset number back to original start number"""
        self.count = -1 
        self.current_num = self.start 

# instantiate 
# serial = SerialGenerator(100)
# serial.generate() 
# serial.reset() 