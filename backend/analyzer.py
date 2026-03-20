import pandas as pd

def analyze_patterns(user_solved_titles, dataset):
    pattern_count = {}
    for title in user_solved_titles:
        rows = dataset[dataset["title"] == title]
        for tags in rows["tags"].dropna():
            tag_list = tags.split(",")
            for tag in tag_list:
                tag = tag.strip()
                pattern_count[tag] = pattern_count.get(tag, 0) + 1
    return pattern_count

def find_weak_patterns(patterns):
    weak = []
    for p, count in patterns.items():
        if count < 10:
            weak.append(p)
    return weak