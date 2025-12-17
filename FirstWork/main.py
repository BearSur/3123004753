import math
from collections import Counter


def cosine_similarity(text1, text2):
    """Calculate cosine similarity between two texts."""
    words1 = list(text1)
    words2 = list(text2)

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    all_words = set(counter1.keys()) | set(counter2.keys())

    vec1 = [counter1.get(w, 0) for w in all_words]
    vec2 = [counter2.get(w, 0) for w in all_words]

    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


def main():
    orig_path = "orig.txt"
    files_to_check = [
        "orig_add.txt",
        "orig_del.txt",
        "orig_0.8_dis_1.txt",
        "orig_0.8_dis_10.txt",
        "orig_0.8_dis_15.txt",
    ]
    ans_path = "ans.txt"

    with open(orig_path, "r", encoding="utf-8") as f:
        orig_text = f.read().strip()

    results = []
    for file in files_to_check:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().strip()
        sim = cosine_similarity(orig_text, text)
        results.append((file, sim))

    with open(ans_path, "w", encoding="utf-8") as f:
        for file, sim in results:
            f.write(f"{file}: {sim:.2f}\n")


if __name__ == "__main__":
    main()
