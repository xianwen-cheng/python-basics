'''用 dict 统计每个词出现几次
不分大小写（统一转小写再统计）
按出现次数降序排列
输出前 5 名，形如：
test: 4 次
needs: 3 次
整个程序不超过 25 行'''


text = """game test needs automation. automation needs scripts
scripts need maintenance maintenance needs a test engineer.
a test engineer needs patience. patience makes a good test engineer."""
words = text.replace(".", "").split()

counts = {}

for f in words:
    if f in counts:
        counts[f] = counts[f] + 1
    else:
        counts[f] = 1
#counts[f] = counts.get(f,0) + 1
print(counts)

print(sorted(counts.items(), key=lambda x: x[1], reverse=True))
