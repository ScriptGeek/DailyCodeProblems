'''
This problem was recently asked by LinkedIn:

Given two rectangles, find the area of intersection.
'''

class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    # Checks if the given Rectangle "other" is overlapping with the current Rectangle "self"
    def is_overlapping(self, other) -> bool:
        in_range = lambda val, min, max: val >= min <= max
        range_overlap = lambda min1, max1, min2, max2: (in_range(min1, min2, max2) or in_range(max1, min2, max2))
        overlap_check = lambda rect1, rect2: range_overlap(rect1.min_x, rect1.max_x, rect2.min_x, rect2.max_x) and range_overlap(rect1.min_y, rect1.max_y, rect2.min_y, rect2.max_y)
        return overlap_check(self, other) or overlap_check(other, self)

def intersection_area(rect1, rect2):
    area=0
    if rect1.is_overlapping(rect2):
        overlap=Rectangle()
        overlap.min_x = rect1.min_x if rect1.min_x>rect2.min_x else rect2.min_x
        overlap.max_x = rect1.max_x if rect1.max_x<rect2.max_x else rect2.max_x
        overlap.min_y = rect1.min_y if rect1.min_y>rect2.min_y else rect2.min_y
        overlap.max_y = rect1.max_y if rect1.max_y<rect2.max_y else rect2.max_y
        area = (overlap.max_x-overlap.min_x)*(overlap.max_y-overlap.min_y)
    return area

# BBB
# AXXB
# AAA
rect1 = Rectangle(0, 0, 3, 3)
rect2 = Rectangle(1, 1, 3, 2)

print(intersection_area(rect1, rect2))
# 2
