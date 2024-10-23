surface_n = int(input())  # the number of points used to draw the surface of Mars.
prev = (0,0)#x,y
landing = []
places = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    if land_y == prev[1]:
        landing = [[prev[0],land_x],prev[1]]
    prev = (land_x,land_y)
    places.append([land_x,land_y])
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate , power = [int(i) for i in input().split()]

    #If speed is quicker than landing speed -> Activate Booster at full power
    if v_speed>=-39:
        power = 0
        print(f"0 {power}")
    else:
        power=4
        print(f"0 {power}")
