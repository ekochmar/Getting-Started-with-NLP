import math

query = [1, 1]
document = [3, 5]

def length(vector):
    sq_length = 0
    for index in range(0, len(vector)):
        sq_length += math.pow(vector[index], 2)
    return math.sqrt(sq_length)
    
def dot_product(vector1, vector2):
    if len(vector1)==len(vector2):
        dot_prod = 0
        for index in range(0, len(vector1)):
            dot_prod += vector1[index]*vector2[index]
        return dot_prod
    else:
        return "Unmatching dimensionality"

cosine =  dot_product(query, document) / (length(query) * length(document))     
print (cosine)
