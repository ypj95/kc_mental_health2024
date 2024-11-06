def load_processed_datasets(path: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Loads the processed datasets, train and test

    Args:
        path (Path): _description_

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: _description_
    """
    pass

def setup_model(model: str, hyperparameters: dict):
        if model == "xgboost":
            return xgb.XGBClassifier(**hyperparameters)
        elif model == "catboost":
            return cat.CatBoostClassifier(**hyperparameters)
        else:
            raise ValueError(f"Model: {model} not implemented.")