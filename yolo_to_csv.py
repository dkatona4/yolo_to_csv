import csv

def unconvert(width, height, x, y, w, h):
    xmax = int((float(x)*width) + (float(w) * width)/2.0)
    xmin = int((float(x)*width) - (float(w) * width)/2.0)
    ymax = int((float(y)*height) + (float(h) * height)/2.0)
    ymin = int((float(y)*height) - (float(h) * height)/2.0)
    return (xmin, ymin, xmax, ymax)

path_of_reading_file = "temp.csv"
output_file = "result.csv"

with open(path_of_reading_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        width = int(row[6])
        height = int(row[7])
        class_id = row[5]
        res = unconvert(width,height,row[1],row[2],row[3],row[4])
        
        print(str(res[0]) + ',' + str(res[1]) + ',' + str(res[2]) + ',' + str(res[3]) + ',' + class_id)
        with open(output_file, "a") as f:
            f.write(row[0] + ',' + str(res[0]) + ',' + str(res[1]) + ',' + str(res[2]) + ',' + str(res[3]) + ',' + '"' + class_id + '"\n')
            f.close()


