def read_input():
    lineOne = map(int, raw_input().split())
    sizes = map(int, raw_input().split())
    bells = lineOne[0]
    boxes = lineOne[1]
    print calculate_box_size(bells, boxes, sizes)

def calculate_box_size(bells, boxes, sizes):
    smallestSize = max(sizes)
    sizes.sort()
    for x in sizes:
        
    return smallestSize

read_input()
