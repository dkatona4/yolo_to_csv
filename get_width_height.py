import csv
import cv2
import numpy

with open("/home/wildhorse_project/camera_trap_wolf/backup/retinanet_ready_csv/ideig.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row[0])
#         im = cv2.imread(("/home/dkatona/sz_zs--wolf/all_pictures/" + row[0]))
        im = cv2.imread(row[0])
        h, w, c = im.shape
        with open("/home/wildhorse_project/camera_trap_wolf/backup/retinanet_ready_csv/width.txt", "a") as f:
            f.write(str(w) + "\n")
            f.close()
        with open("/home/wildhorse_project/camera_trap_wolf/backup/retinanet_ready_csv/height.txt", "a") as f:
            f.write(str(h) + "\n")
            f.close()
