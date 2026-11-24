from dotenv import load_dotenv
import os
import pandas as pd



load_dotenv()
DATA_DIR= os.getenv("DATA_DIR", "./data/")


if __name__ == "__main__":
    df = pd.read_csv(DATA_DIR+"people.csv")
    df["promoted"] = ~df["job_last_promotion_date"].isna()
    company_replace = {"Apple": 4, "Google": 3, "Amazon": 2, "Facebook": 1, "Microsoft": 0}
    position_replace = {"Senior": 2, "Mid": 1, "Junior": 0}
    gender_replace = {"M": 1, "F": 0}

    df = df.replace(company_replace)
    df = df.replace(position_replace)
    df = df.replace(gender_replace)
    
    df.to_csv(DATA_DIR+"prepared_people.csv", sep=",")