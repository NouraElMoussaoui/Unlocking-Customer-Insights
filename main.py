import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from data_loader import load_data

file_path = './data/bank.csv'

df = load_data(file_path)