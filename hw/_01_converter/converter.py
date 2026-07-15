from typing import Iterable
import pandas as pd

class Converter:

    def enumerator(self, values: Iterable[str]) -> dict[str, int]:
        values = [*values]
        enum = {str(values[i]): i for i in range(len(values))}
        return enum


    def columns_mapper(self, columns_str: list[str], df: pd.DataFrame) -> dict[str, dict[str, int]]:
        columns_str = [*columns_str]
        cm = {columns_str[i]: self.enumerator([*df[columns_str[i]].unique()]) for i in range(len(columns_str))}
        return cm


    def convert_x(self, df: pd.DataFrame, mapper: dict[str, dict[str, int]]) -> pd.DataFrame:
        conv = {val: [mapper[val][elem] for elem in df[val]] for val in df.columns}
        return conv

