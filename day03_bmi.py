'''
用 input() 读入身高（米）和体重（公斤）
计算 BMI = 体重 / 身高 ** 2
用 f-string 输出，BMI 保留两位小数，形如：你的 BMI 是 22.86
按中国标准分类输出：
< 18.5 → 偏瘦
18.5 ~ 24 → 正常
24 ~ 28 → 超重
>= 28 → 肥胖
输出形如：你的 BMI 是 22.86，属于：正常
'''
'''
height = float(input("请输入身高/m: "))
weight = float(input("请输入体重/kg: "))

def users_BMI(height,weight):
    bmi = weight / height ** 2
    if bmi < 18.5:
        print(f"你的BMI是{bmi}，属于：偏瘦")
    elif bmi>=18.5 and bmi<24:
        print(f"你的BMI是{bmi}，属于：正常")
    elif bmi>=24 and bmi<28:
        print(f"你的BMI是{bmi}，属于：超重")
    else:
        print(f"你的BMI是{bmi}，属于：肥胖")

users_BMI(height,weight)
'''
'''
bmi = weight / height ** 2
if (bmi < 18.5):
    print(f"你的BMI是{bmi:.2f}，属于：偏瘦")
elif (bmi>=18.5 and bmi<24):
    print(f"你的BMI是{bmi:.2f}，属于：正常")
elif (bmi>=24 and bmi<28):
    print(f"你的BMI是{bmi:.2f}，属于：超重")
else:
    print(f"你的BMI是{bmi:.2f}，属于：肥胖")
'''

def calc_bmi(height,weight):
    bmi = weight / height ** 2
    result = None
    if bmi < 18.5: 
        result = "偏瘦"
    elif bmi < 24: 
        result = "正常"
    elif bmi < 28: 
        result = "超重"
    else: 
        result = "肥胖"
    return bmi, result

assert calc_bmi(1.65, 50.36)[1] == "偏瘦"    # 18.49
assert calc_bmi(1.65, 50.37)[1] == "正常"    # 18.50
assert calc_bmi(1.65, 65.34)[1] == "超重"    # 24.00
assert calc_bmi(1.65, 76.23)[1] == "肥胖"    # 28.00
print("全部通过")

if __name__ == "__main__":
    height = float(input("请输入身高/m: "))
    weight = float(input("请输入体重/kg: "))
    bmi, level = calc_bmi(height, weight)
    print(f"你的BMI是{bmi:.2f}，属于：{level}")