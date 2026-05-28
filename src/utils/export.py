from enum import Enum
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

'''
Utility class that helps save results for the paper in the correct folder.
Works for figures, tables etc. 
'''

# Project Root 
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

class Directory(Enum):
        FIGURE_DIR = ROOT_DIR / "paper" / "figures"
        TABLE_DIR = ROOT_DIR / "paper" / "tables"
        
class PathBuilder:

    @staticmethod
    def build(directory: Directory, filename) -> Path: 
        return Path(directory.value) / filename

def save_figure(fig, filename: str):
    """
    Save a matplotlib figure to figure directory
    """
    path = PathBuilder.build(Directory.FIGURE_DIR, filename=f"{filename}.pdf")

    fig.savefig(path) 

    print(f"Figure: {filename} saved to: {path}")

def save_table(df: pd.DataFrame, filename: str, **kwargs):
    """
    Save pandas dataframe as LaTeX table to paper/tables.
    """
    path = PathBuilder.build(directory=Directory.TABLE_DIR, filename=f"{filename}.tex")

    df.to_latex(path)

    print(f'Table: {filename} saved to: {path}')