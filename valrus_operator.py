"""
海象运算符 (Walrus Operator) := 演示

Python 3.8 引入的新特性，允许在表达式中进行赋值操作。

官方文档: https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
PEP 572: https://www.python.org/dev/peps/pep-0572/

语法：variable := expression

优点：
1. 避免重复计算，提高性能
2. 减少中间变量的使用
3. 让代码更简洁，特别是在列表推导式和while循环中

适用场景：
- 列表推导式中避免重复函数调用
- while循环中需要在条件判断时保存结果
- 正则表达式匹配时保存匹配结果
- 复杂计算中需要多次使用相同结果
"""
import requests as rq
from urllib.parse import urlparse
import re
import random

# ========== 基础示例 ==========
# 海象运算符基础演示：同时赋值和使用值
print(a := True)  # 输出: True
print(f"Value of a: {a}")  # 输出: Value of a: True

# ========== 工具函数 ==========
def is_valid_string(st: str):
    """验证字符串：长度大于3且首字母大写，返回字符编码列表"""
    if len(st) > 3 and st.istitle():
        return [ord(i) for i in st]
    else:
        return False

def return_scheme(st: str) -> str | bool:
    """解析URL并返回协议方案"""
    url = urlparse(st)
    if all([url.scheme, url.netloc]):
        return url.scheme
    else:
        return False

def expensive_calculation(n: int) -> int:
    """模拟一个耗时的计算操作"""
    print(f"执行复杂计算: {n} * {n}")
    return n * n
# ========== 列表推导式优化示例 ==========
items = ["Desk", "ipad", "Hourglass", "tx"]
print("=== 字符串验证示例 ===")

# 传统方式：函数被调用两次（效率低）
print("传统方式（重复调用）:")
filtered = [is_valid_string(item) for item in items if is_valid_string(item)]
print(f"结果: {filtered}")

# 海象运算符方式：函数只调用一次（效率高）
print("海象运算符方式（避免重复调用）:")
filtered = [value for item in items if (value := is_valid_string(item))]
print(f"结果: {filtered}")

# ========== 基础赋值示例 ==========
print("\n=== 基础赋值示例 ===")
print(f"列表长度: {x := len([1,2,3,4])}")  # 输出: 列表长度: 4
print(f"x的值: {x}")  # 输出: x的值: 4

# ========== HTTP请求示例 ==========
print("\n=== HTTP请求示例 ===")
my_url = 'https://www.baidu.com'
print(f"HTTP状态码: {code := rq.get(my_url).status_code}")  # 直接输出状态码
print(f"保存的状态码: {code}")  # 使用保存的状态码

# ========== URL解析示例 ==========
print("\n=== URL解析示例 ===")
print(f"URL方案: {return_scheme('https://www.example.com')}")

urls = ['https://www.google.com', 'www.google.com', 'hwww.example.com', 'ftp://localhost']
print("URL列表:", urls)

# 传统方式：重复解析
print("传统方式（重复解析）:")
valid_url = [return_scheme(url) for url in urls if return_scheme(url)]
print(f"有效URL方案: {valid_url}")

# 海象运算符方式：避免重复解析
print("海象运算符方式（避免重复解析）:")
valid = [scheme for url in urls if (scheme := return_scheme(url))]
print(f"有效URL方案: {valid}")

# ========== while循环示例 ==========
print("\n=== while循环示例 ===")
# 模拟读取数据直到满足条件
def get_data():
    """模拟获取数据的函数"""
    return random.randint(1, 20)

print("查找第一个大于15的数字:")
count = 0
while (data := get_data()) <= 15:
    count += 1
    print(f"第{count}次尝试: {data}")
print(f"找到符合条件的数字: {data}，共尝试了{count}次")

# ========== 正则表达式示例 ==========
print("\n=== 正则表达式示例 ===")
text = "请联系我们: email@example.com 或 phone: 123-456-7890"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 使用海象运算符保存匹配结果
if (match := re.search(pattern, text)):
    print(f"找到邮箱: {match.group()}")
else:
    print("未找到邮箱地址")

# ========== 复杂计算优化示例 ==========
print("\n=== 复杂计算优化示例 ===")
numbers = [2, 3, 4, 5, 6]

print("传统方式（重复计算）:")
result_traditional = []
for n in numbers:
    if expensive_calculation(n) > 10:
        result_traditional.append(n)
print(f"结果: {result_traditional}")

print("海象运算符方式（避免重复计算）:")
result_walrus = []
for n in numbers:
    if (calc_result := expensive_calculation(n)) > 10:
        print(f"计算结果 {calc_result} > 10，添加 {n}")
        result_walrus.append(n)
print(f"结果: {result_walrus}")

# ========== 嵌套表达式示例 ==========
print("\n=== 嵌套表达式示例 ===")
# 在条件表达式中使用海象运算符
scores = [85, 92, 78, 95, 88]
results = []

for score in scores:
    grade = "优秀" if (avg := sum(scores) / len(scores)) < 90 and score > 90 else "良好"
    results.append((score, grade))

print(f"分数列表: {scores}")
print(f"平均分: {sum(scores) / len(scores):.1f}")
print("评分结果:")
for score, grade in results:
    print(f"  {score}: {grade}")

print("\n=== 演示完成 ===")
