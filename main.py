import math

points = [(3,5),(1,7),(5,3),(2,4),(3,1)]

def euclidean_distance(x1, x2):
    return math.sqrt((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2)

def minDisitince(distances):
    min = distances[0];
    for distance in distances:
        if distance < min:
            min = distance
    return min

def main():
    distances = []

    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
            distances.append(euclidean_distance(points[i],points[j]))

    print(minDisitince(distances))

main()