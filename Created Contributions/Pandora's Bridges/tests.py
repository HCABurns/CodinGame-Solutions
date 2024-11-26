def test1():
    coordinates = [
        [1 , 1, 1],
        [-346.67, -291.64, -378.0],
        [482.24, 352.2, -25.63],
        [474.41, -2.42, -41.33],
        [360.39, 197.55, 310.68],
        [-82.04, -105.31, -389.66],
        [-287.02, -83.76, -26.12],
        [-305.79, -196.27, -186.07],
        [-186.87, -80.46, -19.31],
        [113.61, 290.73, -150.65],
        [-8.09, -155.91, -118.89]]
  
    connections = [[6, 8],[0, 10],[0, 8],[7, 10],[5, 7],[1, 5],[0, 9],[2, 3],[2, 9],[0, 4]]
    return coordinates, connections

def valid1():
    coordinates = [
    [1, 1, 1],
    [60.86, 54.79, 0.92],
    [255.06, 191.17, 162.16],
    [266.1, 85.73, 146.52],
    [23.08, 26.13, 29.49],
    [177.46, 23.23, 215.83],
    [205.01, 44.41, 129.06],
    [55.21, 6.36, 295.22],
    [136.08, 108.67, 20.54],
    [10.22, 91.36, 78.93],
    [247.24, 231.4, 152.36]]

    connections = [[2, 10],[0, 4],[1, 4],[3, 6],[4, 9],[1, 8],[2, 3],[3, 5],[5, 7],[3, 8]]
    return coordinates, connections