import pandas as pd
from data_loader import load_data

def preprocess_data():
    """
    Loads the dataset and prepares the variables needed for the research questions. This includes selecting relevant columns and handling any necessary data cleaning steps.
    """
    df = load_data()
    
    columns = [
        'exercise_minutes',
        'sleep_hours',
        'productivity_score',
        'study_hours_per_day',
        'final_grade'
    ]

    df = df[columns]

    return df