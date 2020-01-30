document1 = "meeting ... management ... meeting ... management ... meeting ... management ... meeting ... meeting"

vector = [0, 0]

for word in document1.split(" "):
    if word=="management":
        vector[0] = vector[0] + 1
    if word=="meeting":
        vector[1] = vector[1] + 1
        
print (vector)
