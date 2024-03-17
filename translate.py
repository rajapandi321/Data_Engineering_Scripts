import pandas as pd
import numpy as np
from deep_translator import GoogleTranslator

df = pd.read_excel("C:\Users\rajapandi.gr\Downloads\Versand.csv")

def translate(x):
    if str(x).lower() == 'na':
        return str(x)
    else:
        translated = GoogleTranslator(source='german', target='en').translate(str(x))
        return translated

trans_df=df.apply(np.vectorize(translate))