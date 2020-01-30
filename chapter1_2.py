import math

query = [1, 1]
document = [3, 5]
sq_length = 0

for index in range(0, len(query)):
    sq_length += math.pow((document[index] - query[index]), 2)
    
        
print (math.sqrt(sq_length))
