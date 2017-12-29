import math
def estimate_pi():
    k = 0
    c = ( (2) * ( math.sqrt(2) ) ) /  9801
    total = 0
    while True:
            n = ( math.factorial (4 * k) ) * ( (1103 + (26390 * k) ) )
            d = ( pow (math.factorial (k) , 4) * ( pow (396 , 4 * k) ) )
            temp = c * (n / d)
            total = total + temp
            if abs(temp) < 1e-15 :
                break
            k=k+1
    pi = 1 / total
    return pi

print estimate_pi()
