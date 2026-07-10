from unittest import TestCase, main
from hw_converter.converter import enumerator, columns_mapper, convert_x
import pandas as pd


class TestConverter(TestCase):
    def setUp(self):
        self.df = pd.DataFrame({"Company":['Toyota','Toyota','Hundai', 'Hundai', 'Hundai'], "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']})

    def test_enumerator(self):
        self.assertEqual({'Company': 0, 'Model': 1}, enumerator(self.df.columns))

    def test_columns_mapper(self):
        self.assertEqual({'Company': {'Toyota': 0, 'Hundai': 1}, 'Model': {'Camry': 0, 'Corolla': 1, 'i10': 2, 'Elantra': 3, 'Kona': 4}}, columns_mapper(self.df.columns, self.df))

    def test_convert_x(self):
        self.assertEqual({'Company': [0, 0, 1, 1, 1], 'Model': [0, 1, 2, 3, 4]}, convert_x(self.df, columns_mapper(self.df.columns, self.df)))



if __name__ == "__main__":
    main()