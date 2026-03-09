import pandas as pd
import data_loader as load_data

def preprocess_data():
    """
    Loads the dataset and prepares the variables needed for the research questions. This includes selecting relevant columns and handling any necessary data cleaning steps.
    """
    df = load_data()
    
    columns = [
        "exercise_hours",
        "sleep_hours",
        "productivity_score",
        "study_hours",
        "final_grade"
    ]

    df = df[columns]

    return df