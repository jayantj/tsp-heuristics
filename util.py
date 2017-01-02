import math

def euclidean_dist(location1, location2):
  return math.sqrt(float(((location1[0] - location2[0])**2) + ((location1[1] - location2[1])**2)))

def read_data(filename, limit=None):
  with open(filename) as f:
      points = {}
      for line in f.readlines()[0:limit]:
          line = line.split()
          points[line[0]] = (int(line[1]), int(line[2]))

  distances = {}
  for point1, location1 in points.iteritems():
      for point2, location2 in points.iteritems():
          distance = euclidean_dist(location1, location2)
          if not point1 in distances:
              distances[point1] = {}
          if not point2 in distances:
              distances[point2] = {}
          distances[point1][point2] = distance
          distances[point2][point1] = distance
  return (points, distances)
