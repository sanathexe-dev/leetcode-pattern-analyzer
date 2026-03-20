# Loading the dataset and checking the data
import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())
print(df.info())


# Selecting required columns
columns_needed = [
    "id",
    "title",
    "difficulty",
    "related_topics",
    "acceptance_rate",
    "url",
    "rating",
    "asked_by_faang"
]

df = df[columns_needed]


# Remove duplicate problems
df = df.drop_duplicates(subset=["id"])


# Remove rows with missing topics
df = df.dropna(subset=["related_topics"])


# Cleaning related_topics column
df["related_topics"] = df["related_topics"].str.replace("[", "", regex=False)
df["related_topics"] = df["related_topics"].str.replace("]", "", regex=False)
df["related_topics"] = df["related_topics"].str.replace("'", "", regex=False)


# Capitalizing difficulty column
df["difficulty"] = df["difficulty"].str.capitalize()


# Cleaning acceptance_rate column
df["acceptance_rate"] = df["acceptance_rate"].astype(str)
df["acceptance_rate"] = df["acceptance_rate"].str.replace("%", "", regex=False)
df["acceptance_rate"] = df["acceptance_rate"].astype(float)


# Final cleaning
df["related_topics"] = df["related_topics"].str.strip()

df = df.reset_index(drop=True)


# Save cleaned dataset
df.to_csv("clean_dataset.csv", index=False)

print("Clean dataset created!")

print(df.head())
print("\nDataset Shape:", df.shape)