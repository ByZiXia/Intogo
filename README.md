# Intogo

*Intogo自动注射车相关数据*

## 主要数据：

| 总耗时<sub> （min，T）</sub> | 注射人数<sub>(N)</sub> | 注射剂量<sub>(MBq) </sub> | 注射间隔<sub>(T/N-1)</sub> | 实际总药量<sub>(MBq)</sub> | 预测总药量<sub>(MBq)</sub> |
| :--------------------------: | :--------------------: | :-----------------------: | :------------------------: | :------------------------: | :------------------------: |
|            206.55            |           26           |          266.73           |            8.26            |          15189.39          |          14331.31          |
|            167.42            |           29           |          285.65           |            5.98            |          14379.13          |          14746.13          |
|            192.00            |           32           |          262.48           |            6.19            |          17608.03          |          16398.14          |

>- 第一针起计算方式为从第一个病人开始的总剂量并减去残留药量，即为最理想的用药量。
>- 装药起计算方式为装药时所装载的总剂量。
>- <sub>*因为有时候装上药半个小时都没打针，有时候会浪费100mCi的药，最为理想的状态为装上药就开始打针。*</sub>
>- <sub>误差率计算方式为：（预测总药量-实际总药量）/实际总要量；</sub>

详细数据见primary.excel；



## 进度数据：

| 进度0%<sub>(MBq) </sub> | 进度25%<sub>(MBq) </sub> | 进度50%<sub>(MBq) </sub> | 进度75%<sub>(MBq) </sub> | 进度100%<sub>(MBq) </sub> |
| :---------------------: | :----------------------: | :----------------------: | :----------------------: | :-----------------------: |
|        17120.94         |         10128.59         |         5863.805         |          2187.2          |         359.3402          |
|         17613.2         |         11611.92         |         7143.334         |         3268.914         |         417.4939          |
|        19682.63         |         12715.91         |         7895.315         |         3126.005         |          661.488          |

>此处进度0%为实际工作中最开始的剂量，并非从第一个病人开始的总剂量。  
>
><sub>进度计算方式为：进度25%=每日总注射量*25%</sub>...<sub>例如总注射30个人，第15个就是50%的数据</sub>

- <sub>*因为剂量越大衰变越多，使用平均间隔时间来处理衰变计算对起初的剂量计算较为不准；*</sub>
- <sub>*例如，平均间隔时间为8分钟的话，那么刚开始的8分钟衰变的剂量肯定要远远大于快结束时8分钟衰变的剂量。*</sub>
- <sub> *我在想使用进度来处理衰变计算是否可行？可提供更详细的进度数据，如10%，20%*</sub>...

详细数据见rate.excel；



## 详细推导和公式总结

> 详细见formula.ipnb;



> - 此公式并未手推真实性，仅通过ChatGPT转成python及Excel方式测试计算结果。
> - ChatGPT提示”λ“加”-“是正确的，实际计算中不加”-“时结果较为合理。



## Python计算公式

> 详见formula.py




## Excel计算公式

|      |      A |   B    |    C     |     D      |                              E                               |
| :--: | -----: | :----: | :------: | :--------: | :----------------------------------------------------------: |
|  1   | 总耗时 | 总人数 | 注射剂量 |  注射间隔  |                           预测剂量                           |
|  2   | 219.18 |   26   |  266.73  | =A2/(B2-1) | =C2 * SUMPRODUCT(EXP((LN(2) / 110) * (ROW(INDIRECT("1:" & B2)) - 1) * D2)) |
|  3   | 167.42 |   29   |  285.65  | =A3/(B3-1) | =C3 * SUMPRODUCT(EXP((LN(2) / 110) * (ROW(INDIRECT("1:" & B3)) - 1) * D3)) |
|  4   | 192.00 |   32   |  262.48  | =A4/(B4-1) | =C4 * SUMPRODUCT(EXP((LN(2) / 110) * (ROW(INDIRECT("1:" & B4)) - 1) * D4)) |



> 此表格为演示计算公式如何在Excel中实现，具体数据见primary.excel;



