import pandas as pd
import os

def load(path):
    try:
        pre, ext = os.path.splitext(path)
        if ext.lower() not in (".csv"):
            raise TypeError(f"Format not supported: {ext}")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found {path}")
        data = pd.read_csv(path)
        if data.empty:
            raise FileExistsError("The file is empty. No data to treat")
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except TypeError as terr:
        print(TypeError.__name__ + ":", terr)
    except FileNotFoundError as fnf:
        print(FileNotFoundError.__name__ + ":", fnf)
    except FileExistsError as fe:
        print(FileExistsError.__name__ + ":", fe)
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


print(load("life_expectancy_years.csv"))
print(load("life_expectancy_years.cv"))
print(load("life_expectancy_year.csv"))
print(load("empty.csv"))
