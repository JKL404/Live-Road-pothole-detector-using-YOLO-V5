import torch
import numpy as np
import cv2
import time


def detect_object(frame):
    starting_time = time.time()
    frame_id = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    model = torch.hub.load(
        r'./yolov5', 'custom', path=r'./yolov5/runs/train/yolo_pothole_det_m/weights/best.pt', source='local')
    results = model(frame)
    labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    classes = model.names
    n = len(labels)
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    for i in range(n):
        row = cord[i]
        if row[4] >= 0.2:
            x1, y1, x2, y2 = int(
                row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
            bgr = (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
            cv2.putText(frame, classes[int(
                labels[i])], (x1, y1), font, 0.9, bgr, 2)
        frame_id += 1
    elapsed_time = time.time() - starting_time
    fps = frame_id / elapsed_time
    cv2.putText(frame, "FPS: " + str(round(fps, 2)),
                (40, 670), font, .7, (0, 255, 255), 1)

    ret, buffer = cv2.imencode('.jpg', frame)
    fframe = buffer.tobytes()
    return fframe
