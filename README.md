# Live-Road-pothole-detector-using-YOLO-V5
Road pothole detector using YOLO-V5
YOLO which stands for “You only look once” is one of the most popular object detector in use. The algorithm is designed in a way that by a single pass of forward propagation the network would be able to generate predictions. YOLO achieves very high accuracy and works really well in real time detection.

YOLO take a batch of images of shape (m, 224,224,3) and then outputs a list of bounding boxes along with its confidence scores and class labels, (pc,bx,by,bw,bh,c).


The output generated will be a grid of dimensions S x S ( eg. 19 x 19 ) with each grid having a set of B anchor boxes. Each box will contain 5 basic dimensions which include a confidence score and 4 bounding box information. Along with these 5 basic information, each box will also have the probabilities of the classes. 
