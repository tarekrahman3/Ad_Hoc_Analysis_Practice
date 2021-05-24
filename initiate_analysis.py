""" 
    Objectives:
1. Identify the question the report needs to answer
2. Keep reports visually simple
3. Consider the report layout
4. Make aggregated data points easily accessible
5. Maintain report design consistency
6. Using reporting templates 

    Learning Resources:
What is ad hoc analysis: https://www.3agsystems.com/blog/what-is-ad-hoc-analysis-and-why-be-careful-with-it
CA Ad Hoc Reporting: https://www.ncaa.org/sites/default/files/ca-ch-11-ad-hoc-reporting.pdf
Pandas DataFrame UltraQuick Tutorial: https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas_tf2-colab&hl=en#scrollTo=NJ-I78_7OFVs
First Steps with TensorFlow: https://developers.google.com/machine-learning/crash-course/first-steps-with-tensorflow/programming-exercises
PyGraphistry-Python visual graph analytics library: https://github.com/graphistry/pygraphistry
Hatchet-Python-based library: https://github.com/hatchet/hatchet
Learn TensorFlow in 24 Hours: https://books.google.com.bd/books?id=wCAGEAAAQBAJ&pg=PT101&lpg=PT101&dq=tensorflow&source=bl&ots=2sNrY0plGj&sig=ACfU3U3SfHmVjaog0clg4eTSqCff-oZrJg&hl=en&sa=X&ved=2ahUKEwjckrSw6-DwAhVa4XMBHVc5D0UQ6AEwIHoECBcQAw#v=onepage&q=tensorflow&f=false
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def csv_read():
	originalDict = pd.read_csv(Path('Datasets/bestsellers with categories.csv'))
	return originalDict

df = csv_read()
# To be updated
