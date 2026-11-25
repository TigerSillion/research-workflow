# 个人科研工作流 · Codex × ChatGPT

选一篇你真正想弄懂的论文，挑出其中一张图、一行数字或一个推导。读完后，能否关掉论文，解释它为什么成立，再亲手把它做出来？

## 从一项真实复现开始

第一次使用，建议先给自己两分钟：如果四组数据的回归直线和 R² 几乎相同，你对四张散点图有什么预测？把预测写下来，再运行示例。需要 Git 和 Python 3.8+，脚本仅使用标准库。

```sh
git clone https://github.com/TigerSillion/research-workflow.git
cd research-workflow
python examples/anscombe/reproduce.py
```

Windows 也可用 `py -3`，Linux/macOS 可用 `python3`。终端会输出四组拟合值和判定；打开生成的 `examples/anscombe/output/figure.svg` 看哪里猜错了。[案例、数据出处和结果解读](examples/anscombe/README.md)

## 用自己的问题开题

```sh
python scripts/new_study.py "../studies/my-first-paper" --question "作者图 2 的效应在什么条件下成立？"
```

用 Codex 打开新建的课题目录，发一句「读 AGENTS.md 和 handoff.md，从下一项开始」。在 ChatGPT 中可以上传同两份文件，以及这次要读的论文或最新结果。将讨论中形成的预测、证据或改动交回 Codex 写入课题文件，即可跨工具接续。

| 阶段 | 本轮实际要做的事 | 留下什么 |
|---|---|---|
| 定题和读文献 | 选一个能被数据推翻的主张，定位原文图表；顺引一个基础方法，逆查一次质疑或复现 | `question.md`、`sources.md` |
| 学懂方法 | 自己画因果链、写公式或伪代码，闭卷解释；让 ChatGPT 追问假设与反例 | `learning.md` |
| 重建基线 | 填数据版本、切分、参数、单位和计算口径；写下预期值、容差和理由 | `protocol.md` |
| 运行与质疑 | 用 Codex 执行命令并保留输出；先查输入与中间量，再查最终数字 | `runs.md`、`artifacts/` |
| 探索和交接 | 每次只改变一个有解释力的条件，保留负结果；标明哪些结论能迁移 | `report.md`、`handoff.md` |

没有作者代码时按方法章节独立实现，注明自行补足的假设。理论课题可把数值基线换成“小规模特例＋独立推导”；实验科学可用公开测量数据重做分析，并单列需要设备才能验证的部分。

## 交给哪一个工具

- **ChatGPT 适合讨论。** 例如「围绕论文图 2 只问我三个问题，让我解释观察量、隐藏假设和一个可能反例。等我回答后再指出漏洞。」
- **Codex 适合执行。** 例如「读 protocol.md，先复核输入版本和指标口径，运行最小复现，把命令、实测值和差值追加到 runs.md。运行失败也记录原始报错。」
- **人来做科研判断。** 看结果前写预测；出现分歧时回到原文和原始数据。将自己的解释、证据支持到哪里、下一个区分性实验分别写清楚。

[工具接力与研究提示词](guide.md) · [仓库级 Codex 指令](AGENTS.md) · [可选的工具说明文件](SKILL.md)

## 设计来源

参考 [skJack/research-workflow](https://github.com/skJack/research-workflow) 的固定课题目录、文献整理、基线复现、逐次实验记录和跨会话交接。本仓库针对 Codex 与 ChatGPT 重新编写流程、模板、Python 脚本与示例。
