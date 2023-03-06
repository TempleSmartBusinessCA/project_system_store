import pandas as pd
import date

date = date.get_date()

df = pd.DataFrame(
    {
        "name":["Juan","Manuel","Irma"],
        "Age": [58,34,81],
        "Sex":["Male","Male","Female"]

    }
)

print(df)
print(df["name"])
print(df["Age"].max())

df.to_csv(f"{date}.csv", index=False)

df.info()
