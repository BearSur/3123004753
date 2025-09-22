import math
from collections import Counter

def cosine_similarity(text1, text2):
    """计算两个文本的余弦相似度"""
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
    # 这里直接指定文件名，就像 C++ 里写死路径一样
    orig_path = "orig.txt"
    copy_path = "orig_add.txt"
    ans_path = "ans.txt"

    with open(orig_path, "r", encoding="utf-8") as f:
        text1 = f.read().strip()
    with open(copy_path, "r", encoding="utf-8") as f:
        text2 = f.read().strip()

    similarity = cosine_similarity(text1, text2)

    with open(ans_path, "w", encoding="utf-8") as f:
        f.write(f"{similarity:.2f}")

if __name__ == "__main__":
    main()
