import math
from collections import Counter
import cProfile
def cosine_similarity(text1: str, text2: str) -> float:
    """计算两个文本的余弦相似度"""
    # 将文本按字分割
    words1 = list(text1)
    words2 = list(text2)

    # 统计字频
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # 构造所有词的并集
    all_words = set(counter1.keys()) | set(counter2.keys())

    # 构造向量
    vec1 = [counter1.get(w, 0) for w in all_words]
    vec2 = [counter2.get(w, 0) for w in all_words]

    # 计算余弦相似度
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

def process_files(orig_path: str, files_to_check: list[str], ans_path: str):
    """处理多个文件，计算相似度，并写入结果"""
    with open(orig_path, "r", encoding="utf-8") as f:
        orig_text = f.read().strip()

    results = []
    for file in files_to_check:
        try:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read().strip()
            sim = cosine_similarity(orig_text, text)
            results.append((file, sim))
        except FileNotFoundError:
            results.append((file, "文件未找到"))

    with open(ans_path, "w", encoding="utf-8") as f:
        for file, sim in results:
            if isinstance(sim, float):
                f.write(f"{file}: {sim:.2f}\n")
            else:
                f.write(f"{file}: {sim}\n")

    return results


def main():
    # 原文文件
    orig_path = "orig.txt"

    # 要检测的多个抄袭版文件
    files_to_check = [
        "orig_add.txt",
        "orig_del.txt",
        "orig_0.8_dis_1.txt",
        "orig_0.8_dis_10.txt",
        "orig_0.8_dis_15.txt",
    ]

    # 输出结果文件
    ans_path = "ans.txt"

    return process_files(orig_path, files_to_check, ans_path)

if __name__ == "__main__":
    cProfile.run("main()")

