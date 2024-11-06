import pandas as pd

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
