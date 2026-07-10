from typing import Iterable
import pandas as pd


def enumerator(values: Iterable[str]) -> dict[str, int]:
    values = [*values]
    enum = {str(values[i]): i for i in range(len(values))}
    return enum


def columns_mapper(columns_str: list[str], df: pd.DataFrame) -> dict[str, dict[str, int]]:
    columns_str = [*columns_str]
    cm = {columns_str[i]: enumerator([*df[columns_str[i]].unique()]) for i in range(len(columns_str))}
    return cm


def convert_x(df: pd.DataFrame, mapper: dict[str, dict[str, int]]) -> pd.DataFrame:
    conv = {val: [mapper[val][elem] for elem in df[val]] for val in df.columns}
    return conv


# df = {"Company":['Toyota','Toyota','Hundai', 'Hunday', 'Hunday'], "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']}
# df = pd.DataFrame({"Company":['Toyota','Toyota','Hundai', 'Hundai', 'Hundai'], "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']})
# print(enumerator(df.columns))
# print(columns_mapper(df.columns, df))
# print(convert_x(df, columns_mapper(df.columns, df)))
