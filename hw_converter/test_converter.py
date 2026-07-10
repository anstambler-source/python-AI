from unittest import TestCase, main
from hw_converter.converter import Converter
import pandas as pd

conv = Converter()
df = pd.DataFrame({"Company":['Toyota','Toyota','Hundai', 'Hundai', 'Hundai'], "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']})

class TestConverter(TestCase):

    def test_enumerator(self):
        self.assertEqual({'Company': 0, 'Model': 1}, conv.enumerator(df.columns))

    def test_columns_mapper(self):
        self.assertEqual({'Company': {'Toyota': 0, 'Hundai': 1}, 'Model': {'Camry': 0, 'Corolla': 1, 'i10': 2, 'Elantra': 3, 'Kona': 4}}, conv.columns_mapper(df.columns, df))

    def test_convert_x(self):
        self.assertEqual({'Company': [0, 0, 1, 1, 1], 'Model': [0, 1, 2, 3, 4]}, conv.convert_x(df, conv.columns_mapper(df.columns, df)))



if __name__ == "__main__":
    main()