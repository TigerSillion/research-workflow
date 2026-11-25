---
name: research-workflow
description: 为跨学科研究建立课题目录，整理原始文献、复现图表或推导、记录基线和反例，并在 Codex 与 ChatGPT 会话间交接。用于开题、读论文、复现实验、分析差异或接续研究。
---

从用户的问题中确定一个可核查的最小结果。读取本文件同目录的 guide.md，按课题性质选计算、理论或实验路径。

新课题用 Python 调用本目录的 scripts/new_study.py，将目标设为用户的课题目录，并传入 --question。已有课题先读该课题的 AGENTS.md 和 handoff.md，保留既有笔记。没有文件或执行能力时，为用户生成可以直接粘贴的 Markdown 增量，并明确哪些步骤待运行。

需要公开样例时用 examples/anscombe/README.md。完成一轮后，列出实测或推导、证据位置、尚未解决的差异，并写下一项具体动作。
