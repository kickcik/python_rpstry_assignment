# 삼각형 넓이
def triange_area(a: float, h: float) -> float:
    return a*h*0.5
# 원의 넓이
def circle_area(radius: float) -> float:
    return 3.141592*radius**2
# 직육면체의 넓이
def cuboid_area(x: float, y: float, h: float) -> float:
    return (x*y+x*h+y*h)*2