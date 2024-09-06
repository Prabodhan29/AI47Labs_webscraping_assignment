import pandas as pd
import joblib
from enum import Enum

#! Enum for all the states abbreviations
class State(Enum):
    AL = 1
    AK = 2
    AZ = 3
    AR = 4
    CA = 5
    CO = 6
    CT = 7
    DE = 8
    FL = 9
    GA = 10
    HI = 11
    ID = 12
    IL = 13
    IN = 14
    IA = 15
    KS = 16
    KY = 17
    LA = 18
    ME = 19
    MD = 20
    MA = 21
    MI = 22
    MN = 23
    MS = 24
    MO = 25
    MT = 26
    NE = 27
    NV = 28
    NH = 29
    NJ = 30
    NM = 31
    NY = 32
    NC = 33
    ND = 34
    OH = 35
    OK = 36
    OR = 37
    PA = 38
    RI = 39
    SC = 40
    SD = 41
    TN = 42
    TX = 43
    UT = 44
    VT = 45
    VA = 46
    WA = 47
    WV = 48
    WI = 49
    WY = 50


#! Load the saved model 
model_path = 'model.pkl'
loaded_model = joblib.load(model_path)

#! Add the state for which you want to predict how many awards are given to hospitals in that state.
state_for_prediction = 'NY'

new_data = pd.DataFrame({
    'state_encoded': [state_for_prediction] 
})

predictions = loaded_model.predict(new_data)

#? Display predictions in terminal
print(f"Predicted number of awards for state {state_for_prediction}: {predictions[0]}")
