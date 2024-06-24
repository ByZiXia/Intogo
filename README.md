# Intogo
Intogo自动注射车


## 主要包括数据：

<img width="983" alt="image" src="https://github.com/wang-zixia/Intogo/assets/153195196/72cac08a-ab51-471a-a8e0-bcd1a17f6fa6">

>此处实际总药量及预测总药量均为从第一个病人打针时开始的总剂量并减去残留药量，既为最真实最理想的用药量。

详细见附表1；

## 进度条数据：

<img width="993" alt="image" src="https://github.com/wang-zixia/Intogo/assets/153195196/cc49e783-2fc8-4fd1-8a61-f9eb36de4249">

>此处进度0%为实际工作中最开始的剂量，并非从第一个病人开始的总剂量。
>
>ps:因为有时候装上药半个小时都没打针，有时候会浪费100mCi的药，最为理想的状态为装上药就开始打针。
>
>因为剂量越大衰变越快，使用平均间隔时间来处理衰变计算对起初的剂量计算较为不准，我在想使用进度来处理衰变计算是否可行？
>
>例如，平均间隔时间为8分钟的话，那么刚开始的8分钟衰变的剂量肯定要远远大于快结束时8分钟衰变的剂量。
>
详细见附表2；

## python计算代码
``` py
importnumpy asnp


defcalculate_initial_dose(D, N, total_time):
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

    returntotal_dose


# 示例参数
D = 266.85         # 每人药物剂量 (MBq)
N = 30            # 注射人数
total_time = 237      # 总耗时 (分钟)
# 计算初始药物量
initial_dose = calculate_initial_dose(D, N, total_time)
print("需要准备的初始药物量：", initial_dose, "MBq")
![image](https://github.com/wang-zixia/Intogo/assets/153195196/6c6020ed-5242-45f5-a685-be6f6fa52c7f)


$$1. 衰变常数：
λ=ln⁡(2)110\lambda = \frac{\ln(2)}{110}λ=110ln(2)
	2. 每个病人的注射间隔时间：
Δt=TN−1\Delta t = \frac{T}{N-1}Δt=N−1T
	3. 每次注射的时间点：
ti=i⋅Δt,其中i=0,1,2,…,N−1t_i = i \cdot \Delta t, \quad \text{其中} \quad i = 0, 1, 2, \ldots, N-1ti=i⋅Δt,其中i=0,1,2,…,N−1
	4. 每次注射时的实际药物量：
di=D⋅e−λtid_i = D \cdot e^{-\lambda t_i}di=D⋅e−λti
	5. 总药物量：
Dtotal=∑i=0N−1di=∑i=0N−1D⋅e−λi⋅ΔtD_{\text{total}} = \sum_{i=0}^{N-1} d_i = \sum_{i=0}^{N-1} D \cdot e^{-\lambda i \cdot \Delta t}Dtotal=i=0∑N−1di=i=0∑N−1D⋅e−λi⋅Δt
将上述公式合并，得到总药物量的计算公式：
Dtotal=D⋅∑i=0N−1e−λi⋅TN−1D_{\text{total}} = D \cdot \sum_{i=0}^{N-1} e^{-\lambda i \cdot \frac{T}{N-1}}Dtotal=D⋅i=0∑N−1e−λi⋅N−1T![image](https://github.com/wang-zixia/Intogo/assets/153195196/95f55b4b-6ef8-4962-a94b-a6767949a8eb)$$



