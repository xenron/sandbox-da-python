import math
import numpy as np


def question01(begin, end):
    target = range(begin, end)
    return sum(math.pow(x, 2) for x in target)


def question02(arr):
    print("Internal rate of return", np.irr(arr))


def question03(apr, stage, amount):
    print("Payment", np.pmt(apr, stage, amount))

if __name__ == '__main__':
    print("\n========= question01 =========")
    # 1^2+2^2+......+10^2
    print(question01(1, 11))
    print("\n========= question02 =========")
    question02([-2000, 800, 1600])
    print("\n========= question03 =========")
    question03(0.06/12, 12 * 5, 20000)
    print("\n========= finish =========")

