import json
import argparse
from datetime import date
from pathlib import Path

DATA_FILE = Path("expenses.json")   


def load_expenses():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(args):
    expenses = load_expenses()
    new_id = max((e["id"] for e in expenses), default=0) + 1
    expense = {
        "id": new_id,
        "title": args.title,
        "amount": args.amount,
        "category": args.category,
        "date": args.date or str(date.today()),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added: #{new_id} {args.title} - Rs.{args.amount}")


def list_expenses(args):
    expenses = load_expenses()
    if args.category:
        expenses = [e for e in expenses if e["category"] == args.category]
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<4}{'Date':<12}{'Category':<12}{'Title':<20}{'Amount':>8}")
    print("-" * 56)
    for e in expenses:
        print(f"{e['id']:<4}{e['date']:<12}{e['category']:<12}{e['title']:<20}{e['amount']:>8}")


def delete_expense(args):
    expenses = load_expenses()
    new_list = [e for e in expenses if e["id"] != args.id]
    if len(new_list) == len(expenses):
        print("Expense ID not found.")
        return
    save_expenses(new_list)
    print(f"Deleted expense #{args.id}")


def update_expense(args):
    expenses = load_expenses()
    for e in expenses:
        if e["id"] == args.id:
            if args.title:    e["title"] = args.title
            if args.amount:   e["amount"] = args.amount
            if args.category: e["category"] = args.category
            save_expenses(expenses)
            print(f"Updated expense #{args.id}")
            return
    print("Expense ID not found.")


def summary(args):
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    total = sum(e["amount"] for e in expenses)
    by_category = {}
    for e in expenses:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
    print(f"Total spent: Rs.{total}")
    print("By category:")
    for cat, amt in by_category.items():
        print(f"  {cat}: Rs.{amt}")


def main():
    parser = argparse.ArgumentParser(description="Simple Expense Tracker CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add an expense")
    p_add.add_argument("title")
    p_add.add_argument("amount", type=float)
    p_add.add_argument("--category", default="general")
    p_add.add_argument("--date", help="YYYY-MM-DD (default: today)")
    p_add.set_defaults(func=add_expense)

    p_list = sub.add_parser("list", help="List expenses")
    p_list.add_argument("--category")
    p_list.set_defaults(func=list_expenses)

    p_del = sub.add_parser("delete", help="Delete an expense")
    p_del.add_argument("id", type=int)
    p_del.set_defaults(func=delete_expense)

    p_upd = sub.add_parser("update", help="Update an expense")
    p_upd.add_argument("id", type=int)
    p_upd.add_argument("--title")
    p_upd.add_argument("--amount", type=float)
    p_upd.add_argument("--category")
    p_upd.set_defaults(func=update_expense)

    p_sum = sub.add_parser("summary", help="Show totals")
    p_sum.set_defaults(func=summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()