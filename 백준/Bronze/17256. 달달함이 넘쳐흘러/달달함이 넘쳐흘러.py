a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())

print(int(c_x - a_z), int(c_y / a_y), int(c_z - a_x))