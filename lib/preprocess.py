import pandas as pd
import re

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [x.lower().replace(" ", "_") for x in df.columns.to_list()]
    return df.rename(columns={
            "have_you_ever_had_suicidal_thoughts_?": "has_suicidal_thoughts",
            "work/study_hours": "work_study_hours",
            "working_professional_or_student": "job",
            "dietary_habits": "diet"
    })
    
def clean_column_diet_habits(df: pd.DataFrame) -> pd.DataFrame:
    diet_habit_mapping = {
        "Healthy": "Healthy",
        "Unhealthy": "Unhealthy",
        "Moderate": "Moderate",
        "More Healthy": "Healthy",
        "Less than Healthy": "Unhealthy",
        "No Healthy": "Unhealthy",
        "Less Healthy": "Unhealthy"
    }
    return df.assign(diet=df["diet"].apply(lambda x: diet_habit_mapping.get(x, "nan")))

def calculate_avg_sleep(x):
    hour = re.search(r'(\d+-?\d*)', x)
    if hour == None:
        return float('nan')
    splits = hour.group(1).split("-")
    
    # if real range is given
    if len(splits) > 1:
        avg_sleep = int(splits[0]) + int(splits[1])/2
    else:
        avg_sleep = int(splits[0])
    
    return avg_sleep


def clean_sleep_column(df: pd.DataFrame, bin=False) -> pd.DataFrame:
    """Returns sleep duration as average or category from 0 to 5

    Args:
        df (pd.DataFrame): _description_
        bin (bool, optional): _description_. Defaults to False.

    Returns:
        pd.DataFrame: _description_
    """
    df["sleep_duration"] = df["sleep_duration"].apply(calculate_avg_sleep).dropna()
    if bin:
        df["sleep_duration"] = pd.cut(df["sleep_duration"], 5, labels=range(5))
    return df


def clean_profession_column(x: pd.DataFrame, min_sample_size: int = 30) -> pd.DataFrame:
    """Clean all professions which have less than 30 samples => make profession NaN or Other.
    """
    profession_dist = x["profession"].value_counts()
    ids = (profession_dist > min_sample_size).values
    professions_to_agg = profession_dist[~ids].to_dict()
    professions_to_agg = dict(zip(list(professions_to_agg.keys()), ['other']*len(professions_to_agg)))
    return x.assign(profession=x["profession"].apply(lambda x: professions_to_agg[x] if x in professions_to_agg else x))
