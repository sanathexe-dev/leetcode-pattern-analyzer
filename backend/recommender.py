import pandas as pd
from leetcode_api import get_recent_submissions

def recommend_problems_logic(recent_problems):
    try:
        # Load the dataset
        df = pd.read_csv("clean_dataset.csv")
        
        # Based on your CSV, the column is 'related_topics'
        topic_col = 'related_topics'
        title_col = 'title'

        if topic_col not in df.columns or title_col not in df.columns:
            return ["CSV Structure Error"], ["Ensure columns match: title, related_topics"]

        # 1. Extract all unique topics from the dataset
        # Since one row can have multiple topics, we split them
        all_topics_set = set()
        for topics in df[topic_col].dropna():
            for t in topics.split(','):
                all_topics_set.add(t.strip())
        
        # 2. Identify topics user HAS done recently
        recent_problems_lower = [p.lower() for p in recent_problems]
        done_topics = set()
        recent_matches = df[df[title_col].str.lower().isin(recent_problems_lower)]
        
        for topics in recent_matches[topic_col].dropna():
            for t in topics.split(','):
                done_topics.add(t.strip())

        # 3. Weak areas = topics available but not in recent history
        weak_topics = [t for t in sorted(list(all_topics_set)) if t not in done_topics]
        
        # Fallback if history is empty
        if not weak_topics:
            weak_topics = sorted(list(all_topics_set))[:3]
        
        # 4. Filter recommendations from those weak topics
        # We find problems where the 'related_topics' string contains one of the weak topics
        target_weak = weak_topics[0] if weak_topics else ""
        recommendations = df[df[topic_col].str.contains(target_weak, na=False, case=False)][title_col].head(8).tolist()
        
        return weak_topics[:3], recommendations

    except FileNotFoundError:
        return ["File Missing"], ["clean_dataset.csv not found in backend/"]
    except Exception as e:
        print(f"Recommender Error: {e}")
        return ["Logic Error"], [str(e)]