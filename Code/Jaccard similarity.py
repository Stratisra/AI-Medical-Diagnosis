from scipy.spatial.distance import jaccard
from sklearn.metrics import jaccard_score
import csv

topDis_str = ['None', 'None', 'None']
topDis_float = [0.0, 0.0, 0.0]
A = []
B = []
    
# Input the array of symptoms provided by the user
try:
    with open('Symptoms.csv', 'r') as file:
        readCSV = list(csv.reader(file, delimiter=','))
        A = [float(x) for x in readCSV[0]]

#Print error if the file is not found
except FileNotFoundError:
    print("Symptoms.csv file not found or could not be read.")
    exit()

with open('Healthcare dataset_cropped_final.csv', 'r') as file1, open('Healthcare dataset_Disease Names.csv', 'r') as file2, open('topDis.csv', 'w') as f_output:
    readCSV1 = list(csv.reader(file1, delimiter=','))
    readCSV2 = list(csv.reader(file2, delimiter=','))
    write = csv.writer(f_output, delimiter=',')
    row2 = readCSV2[0]
    x = 0

    # Check Jaccard Similarity
    for x in range(149):
        B = [float(x) for x in readCSV1[x]]
        distance = round(jaccard(A, B) * 100, 2)
        similarity = round(jaccard_score(A, B) * 100, 2)

        # Find the diseases with the most probability
        if similarity > topDis_float[0]:
           topDis_float[2] = topDis_float[1]
           topDis_float[1] = topDis_float[0]
           topDis_float[0] = similarity
           topDis_str[2] = topDis_str[1]
           topDis_str[1] = topDis_str[0]
           topDis_str[0] = str(row2[x])
        elif similarity > topDis_float[1]:
           topDis_float[2] = topDis_float[1]
           topDis_float[1] = similarity
           topDis_str[2] = topDis_str[1]
           topDis_str[1] = str(row2[x])
        elif similarity > topDis_float[2]:
           topDis_float[2] = similarity
           topDis_str[2] = str(row2[x])
    
    topDis = [[topDis_str[0], topDis_float[0]], [topDis_str[1], topDis_float[1]], [topDis_str[2], topDis_float[2]]]

    for y in range(3):
        write.writerow(topDis[y])
        print("Number", y + 1, "most probable disease:", topDis_str[y], ",", topDis_float[y], "%")