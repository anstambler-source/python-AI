from ultralytics import YOLO
from pandas import DataFrame

class ImageInfo:
    def __init__(self, path):
        self.path = path
        self.model = YOLO('yolov8m-seg.pt')
        self.results = self.model(path)
        self.boxes = self.results[0].boxes
        self.xyxy = self.boxes.xyxy.cpu().numpy()
        self.classes = self.boxes.cls.cpu().numpy()
        self.all_names = self.results[0].names
        self.confidence = self.boxes.conf.cpu().numpy()
        self.names = [self.all_names[val] for val in self.classes]
        self.xywhn = self.boxes.xywhn.cpu().numpy()
        self.xyxyn = self.boxes.xyxyn.cpu().numpy()

    def boxes_class(self, name: str):
        res = [ind for ind, val in enumerate(self.classes) if self.all_names[val] in name]
        return res

    def box_info(self, index):
        xyxy = (round(float(item), 5) for item in self.xyxy[index])
        confidence = round(float(self.confidence[index]), 5)
        name = self.all_names[self.classes[index]]
        return (*xyxy, confidence, name)

    def data_frame(self):
        df = DataFrame(self.xyxy, columns=['xmin', 'ymin', 'xmax', 'ymax'])
        df['name'] = self.names
        df['confidence'] = self.confidence
        return df

    def suitcase_handbag_person(self, threshold):
        list_suitcase_handbag = self.boxes_class('suitcasehandbag')
        centers_s_h = {index: self.xywhn[index][:2] for index in list_suitcase_handbag}
        d = {}

        for s_h in list_suitcase_handbag:
            best_person = None
            best_distance = threshold + 1

            for person in self.boxes_class('person'):
                x_min, y_min, x_max, y_max = self.xyxyn[person]
                if x_min <= centers_s_h[s_h][0] <= x_max and y_min <= centers_s_h[s_h][1] <= y_max:
                    distance_c = self._distance_centers(person, s_h)
                    if distance_c < best_distance:
                        best_distance = distance_c
                        best_person = person

            if best_distance <= threshold:
                d[s_h] = (best_person, round(float(best_distance), 5))
            else:
                d[s_h] = None

        return d

    def _distance_centers(self, el_1, el_2):
        x_1, y_1 = self.xywhn[el_1][:2]
        x_2, y_2 = self.xywhn[el_2][:2]
        return ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
