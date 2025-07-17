pi = 3.141592

def number_input() -> float:
    return float(input("반지름을 입력하세요 : "))

def get_circum(redius):
    return 2*pi*redius

def get_circle(redius):
    return pi*redius**2