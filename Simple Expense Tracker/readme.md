# 💰 Simple Expense Tracker

A minimal command-line **expense tracker** written in Python that saves your expenses locally using a **JSON file**.
No databases, no setup — just run and start tracking.

---

## 🚀 Features

- Add expenses with amount, category, and description
- Automatically timestamps each entry
- View total spending and category breakdown
- Data is stored persistently in a local `expenses.json` file
- No external libraries required

---

## 🧠 Example Usage

```bash
$ python expense_tracker.py
📘 Simple Expense Tracker

Choose an option:
1️⃣ Add expense
2️⃣ View summary
3️⃣ Exit
> 1
Amount: $12.5
Category: Food
Description: Lunch
✅ Added 12.5 in 'Food' category.

> 2
💵 Total Expenses: $12.50

- Food: $12.50
```


## 🛠️ Requirements

* Python 3.x

  No dependencies — it uses only the built-in `json`, `datetime`, and `pathlib` modules.

  ## 📂 Project Structure

  `expense-tracker/
  │
  ├── expense_tracker.py   # main script
  ├── expenses.json        # generated data file
  └── README.md            # documentation`
