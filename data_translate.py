num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int数据类型为",type(num_int))
print("num_flo数据类型为",type(num_flo))
print("num_new数据类型为",type(num_new),"值为：",num_new)

num_int = 123
num_str = "456"
print(num_int + int(num_str))

x = int(2.8)
y = int("23")
z = float("33")

print(x," ", y," ",z)

print(oct(1456))