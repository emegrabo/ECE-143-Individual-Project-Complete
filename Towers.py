class Tower:
    """ Tower class
    """

    def __init__(self, start, width, height):
        """Initialization of the Tower Object
        Arguments:
            start {tuple} -- bottom left hand corner of the tower's coverage (x,y)
            width {int} -- width of the tower's coverage (x-axis)
            height {int} -- height of the tower's coverage (y-axis)
        """
        assert isinstance(start,tuple) and len(start) == 2, "start invalid"
        assert start[0] >= 0 and start[1] >= 0, "start must have positive values"
        assert isinstance(height,int) and height > 0, "Height must be integer > 0"
        assert isinstance(width, int) and width > 0, "Width must be integer > 0"

        self.start = start
        self.height = height
        self.width = width

    def __repr__(self):
        """Tower representation
        """
        return "Bottom Left Corner = %s, Width = %s, Height = %s" % (self.start, self.width, self.height)

    def __eq__(self, other):
		"""Checks if two towers have the same coverage location and size
		"""
		assert isinstance(other,Tower), "other not a Tower"
		if self.start == other.start and self.width == other.width and self.height == other.height:
			return True
		else:
			return False

    def __lt__(self,other):
		"""checks if self covers any part to the left of other
		"""
		assert isinstance(other,Tower), "other not a Tower"
		if self.start[0] < other.start[0]:
			return True
		else:
			return False

    def __gt__(self,other):
		"""checks if self covers any part to the right of other
		"""
		assert isinstance(other,Tower), "other not a Tower"
		if self.right_edge > other.right_edge:
			return True
		else:
			return False

    def __le__(self,other):
		"""Returns true if there is coverage below other's coverage
		"""
		assert isinstance(other,Tower), "other not a Tower"
		if self.start[1] < other.start[1]:
			return True
		else:
			return False

    def __ge__(self,other):
		"""Returns true if there is coverage above other's coverage
		"""
		assert isinstance(other,Tower), "other not a Tower"
		if self.top_edge > other.top_edge:
			return True
		else:
			return False

    @property
    def right_edge(self):
        """gets the value at the right edge of coverage
        """
        return self.start[0] + self.width

    @property
    def top_edge(self):
        """gets the value the top edge of coverage
        """
        return self.start[1] + self.height

    def intersects(self,other):
		"""Checks if the tower intersects with the other tower
		"""
		assert isinstance(other,Tower), "other not a tower"
		if ((self.start[0]+self.width) <= other.start[0]):
			return False
		if (self.start[0] >= (other.start[0]+other.width)):
			return False
		if (self.start[1] >= (other.start[1]+other.height)):
			return False
		if ((self.start[1]+self.height) <= other.start[1]):
			return False
		else:
			return True