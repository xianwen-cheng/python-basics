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