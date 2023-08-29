# TicTacToe Pro

- 一个练手的项目 / A practice project.

- 有很多bug，但至少能运行对吧 / Lots of bugs, but at least it works, right?

- 有些地方计算不知道对不对 / I don't know if it's calculating correctly in some places

- `streamlit run main.py`

- 建议用3或4模式 / Mode 3 or 4 is recommended

- 英文嘛……看心情 / English support ...... I don't know if there will be

---

1. 首先计算生成了带有胜负的井字棋所有结局 / First, all endings of tic-tac-toe with a winner were computed

2. 导入到数据库中，不去重（我觉得重复的结局代表它有多种不同的方式可以导向这个结局） / Imported into the database without removing duplicates (because I think a duplicate ending means it has multiple different ways to lead to that ending)

3. 运行时计算它下各个地方时胜负平的结局个数 / Calculate the number of win/lose tie-break endings at runtime when it plays in each place.

4. 处理一下就返回 / Process the data and return the result


