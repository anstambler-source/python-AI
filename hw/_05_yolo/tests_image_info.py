from unittest import main, TestCase
from yolo import ImageInfo
from pathlib import Path


class TestImageInfo(TestCase):

    @classmethod
    def setUpClass(cls):
        image_path = Path(__file__).parent / "street.jpg"
        cls.image = ImageInfo(str(image_path))

    def test_image_created(self):
        self.assertEqual(Path(self.image.path).name, "street.jpg")
        self.assertGreater(len(self.image.xyxy), 0)
        self.assertEqual(len(self.image.classes), len(self.image.xyxy))
        self.assertEqual(len(self.image.names), len(self.image.xyxy))

    def test_boxes_class_person(self):
        persons = self.image.boxes_class("person")

        self.assertIsInstance(persons, list)
        self.assertGreater(len(persons), 0)

        for i in persons:
            self.assertEqual(self.image.names[i], "person")

    def test_boxes_class_suitcase(self):
        suitcases = self.image.boxes_class("suitcase")

        for i in suitcases:
            self.assertEqual(self.image.names[i], "suitcase")

    def test_boxes_class_handbag(self):
        handbags = self.image.boxes_class("handbag")

        for i in handbags:
            self.assertEqual(self.image.names[i], "handbag")

    def test_box_info(self):
        info = self.image.box_info(0)

        self.assertEqual(len(info), 6)

        xmin, ymin, xmax, ymax, conf, name = info

        self.assertLess(xmin, xmax)
        self.assertLess(ymin, ymax)

        self.assertGreaterEqual(conf, 0)
        self.assertLessEqual(conf, 1)

        self.assertIsInstance(name, str)

    def test_dataframe(self):
        df = self.image.data_frame()

        self.assertEqual(len(df), len(self.image.xyxy))

        self.assertEqual(
            list(df.columns),
            ["xmin", "ymin", "xmax", "ymax", "name", "confidence"]
        )

    def test_distance_centers_same_box(self):
        d = self.image._distance_centers(0, 0)

        self.assertEqual(d, 0)

    def test_distance_centers_symmetric(self):
        if len(self.image.xyxy) > 1:
            d1 = self.image._distance_centers(0, 1)
            d2 = self.image._distance_centers(1, 0)

            self.assertAlmostEqual(d1, d2)

    def test_suitcase_handbag_person(self):
        result = self.image.suitcase_handbag_person(1)

        self.assertIsInstance(result, dict)

        for key, value in result.items():
            self.assertIn(self.image.names[key], ("suitcase", "handbag"))

            if value is not None:
                person_index, distance = value

                self.assertEqual(self.image.names[person_index], "person")
                self.assertGreaterEqual(distance, 0)
                self.assertLessEqual(distance, 1)

    def test_threshold_zero(self):
        result = self.image.suitcase_handbag_person(0)

        for value in result.values():
            self.assertIsNone(value)


if __name__ == "__main__":
    main()