import numpy as np


def calculate_initial_dose(D, N, total_time):
    # 衰变常数
    decay_constant = np.log(2) / 110

    # 每个病人的注射间隔时间 (分钟)
    delta_t = total_time / (N - 1)

    # 计算每个时刻的药物量
    injection_times = np.arange(N) * delta_t
    doses = D * np.exp(decay_constant * injection_times)    # 修正衰减公式
                # 此处“decay_constant”ChatGPT提示修正衰减公式，需要加上“-“，但是加上负号计算结果不准。
    # 总药物量
    total_dose = np.sum(doses)

    return total_dose


# 示例参数
D = 266.85         # 每人药物剂量 (MBq)
N = 30             # 注射人数
total_time = 237       # 总耗时 (分钟)
# 计算初始药物量
initial_dose = calculate_initial_dose(D, N, total_time)
print("需要准备的初始药物量：", initial_dose, "MBq")
