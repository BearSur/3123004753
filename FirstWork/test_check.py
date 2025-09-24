import unittest
import os
from main import cosine_similarity, process_files


class TestSimilarity(unittest.TestCase):
    def test_identical_text(self):
        self.assertAlmostEqual(cosine_similarity("今天", "今天"), 1.0, places=2)

    def test_different_text(self):
        self.assertAlmostEqual(cosine_similarity("abc", "xyz"), 0.0, places=2)

    def test_partial_text(self):
        sim = cosine_similarity("今天是星期天", "今天是周天")
        self.assertGreater(sim, 0.5)

    def test_empty_text(self):
        self.assertEqual(cosine_similarity("", ""), 0.0)


class TestProcessFiles(unittest.TestCase):
    def setUp(self):
        # 创建测试文件
        with open("orig.txt", "w", encoding="utf-8") as f:
            f.write("今天是星期天，天气晴，今天晚上我要去看电影。")

        with open("file1.txt", "w", encoding="utf-8") as f:
            f.write("今天是周天，天气晴朗，我晚上要去看电影。")

        self.files = ["file1.txt", "nofile.txt"]
        self.ans_path = "ans.txt"

    def tearDown(self):
        # 清理测试文件
        for fname in ["orig.txt", "file1.txt", "ans.txt"]:
            if os.path.exists(fname):
                os.remove(fname)

    def test_process_files(self):
        results = process_files("orig.txt", self.files, self.ans_path)

        # 检查返回结果
        self.assertEqual(len(results), 2)
        self.assertIsInstance(results[0][1], float)
        self.assertEqual(results[1][1], "文件未找到")

        # 检查输出文件存在
        self.assertTrue(os.path.exists(self.ans_path))
        with open(self.ans_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("file1.txt", content)
        self.assertIn("nofile.txt", content)


if __name__ == "__main__":
    unittest.main()
