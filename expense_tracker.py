from expense import Expense
import datetime
import calendar

def main():
    print("Running Expense Tracker !")
    expense_file_path="expense.csv"
    budget= 2000000

    #get  user input for Expense.
    expense = get_user_expense()
    
    #Write their expense to a file.
    save_expense_to_file(expense,expense_file_path)
    #Read file and Summarize Expense.
    summarize_expense(expense_file_path,budget)

def get_user_expense():
    print(f"get user expense..")
    expense_name=input("Enter Expense name : ")
    expense_amt=float(input("Enter Expense amount : "))
    expense_category = ["🍔 Food", 
                        "🏠 Home", 
                        "💼 Work", 
                        "🎉 Fun", 
                        "📦 Misc"]
    while True:
        print ("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f"  {i+1},  {category_name}") 
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Enter a category number {value_range} :")) -1
        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense( name=expense_name,category=selected_category,amount=expense_amt)
            return new_expense
        else:
            print("Invaild category , Please try again ...")
           
def save_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path,budget):
    print("Summarize user expense...")
    expenses : list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines :
            expense_name, expense_amt,expense_category = line.strip().split(",")
            print(expense_name,expense_amt,expense_category)
            line_expense=Expense(
                name=expense_name , amount=float(expense_amt), category=expense_category
            )
            print(line_expense)
            expenses.append(line_expense)
        print(expenses)
    amount_by_category= {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expense By Category : ")
    for key,amount in amount_by_category.items():
        print(f"  {key}: ₹{amount:.2f}")
    total_spend= sum([ex.amount for ex in expenses])
    print(f"You've spent ₹{total_spend:.2f} this month !")
    remaininng_budget = budget - total_spend
    print(f"Budget remaininng :  ₹{remaininng_budget:.2f} this month !")
    now =datetime.datetime.now()
    day_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = day_in_month - now.day  # Fixed this line
    print(f"Days remaining in the month: {remaining_days}")
    daily_budget = remaininng_budget/ remaining_days
    print(f"Budget Per day : ₹{daily_budget:.2f}")  
    

if __name__== "__main__":
    main()