class Solution:
    def max_deletions(source: str, pattern: str, targetIndices: list) -> int:

        def is_subsequence(s: str, p: str) -> bool:
            """检查 p 是否是 s 的子序列"""
            it = iter(s)
            return all(char in it for char in p)

        max_deletable = 0

        # 尝试删除 targetIndices 中的每个字符
        for idx in targetIndices:
            # 创建新的 source，删除指定的字符
            new_source = source[:idx] + source[idx + 1:]

            # 检查 pattern 是否仍然是 new_source 的子序列
            if is_subsequence(new_source, pattern):
                max_deletable += 1

        return max_deletable

if __name__ == '__main__':

        # 示例调用
    source = "abbaa"
    pattern = "aba"
    targetIndices = [0, 1, 2]
    result = Solution.max_deletions(source,pattern,targetIndices)
    print(f"最多可以进行的删除操作次数: {result}")
