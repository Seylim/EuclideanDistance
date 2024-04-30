def euclideanDistance(points):
    distance = []
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
            distance.append((points[i]-points[j])**2)
