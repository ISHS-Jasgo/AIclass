fahrenheit = float(input("화씨: "))
# (1°C × 9/5) + 32 = 33.8°F
celsius = (fahrenheit - 32.0) * 5/9
print("화씨 %lf도는 섭씨 %lf도이다." % (fahrenheit, celsius))
