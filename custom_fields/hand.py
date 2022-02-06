class Hand:

    def __init__(self, north, east, west, south) -> None:
        self.north = north 
        self.south = south
        self.east = east 
        self.west = west 
    
    def __str__(self) -> str:
        return f"{self.north} {self.east} {self.west} {self.south}"