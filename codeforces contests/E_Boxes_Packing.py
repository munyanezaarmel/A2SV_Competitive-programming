
n = int(input())
boxes = list(map(int, input().split()))

max_side_length = max(boxes)

visible_boxes = sum(1 for box in boxes if box == max_side_length)

print(visible_boxes)
