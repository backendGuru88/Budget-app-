import streamlit as st
import matplotlib.pyplot as plt

st.title("Budget Planner")
st.write("Plan your monthly budget, track your expenses, and achieve your financial goals!")


income = st.number_input("Enter your monthly income:", min_value=0.0, format="%.2f")

expenses = st.text_area(
    "Enter your expenses (one per line, in the format 'category: amount').",
    placeholder="E.g., Rent: 500\nGroceries: 200\nTransportation: 100"
)



# Initialize variables
expense_dict = {}
disposable_income = 0
total_expenses = 0

# 2. Budget Calculation and Summary Display
if st.button("Calculate Budget"):
    try:
        # Parse expenses
        for line in expenses.split("\n"):
            if line.strip():  # Skip empty lines
                category, amount = line.split(":")
                expense_dict[category.strip()] = float(amount.strip())

        # Calculations
        total_expenses = sum(expense_dict.values())
        disposable_income = income - total_expenses

        # Display results
        st.write(f"**Total Expenses:** ${total_expenses:.2f}")
        st.write(f"**Disposable Income:** ${disposable_income:.2f}")
    except ValueError:
        st.error("⚠️ Please enter expenses in the correct format: 'category: amount'.")



if expense_dict:
    st.write("### Expense Distribution")
    fig, ax = plt.subplots()
    ax.pie(expense_dict.values(), labels=expense_dict.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

if disposable_income:
    if disposable_income < 0:
        st.error("⚠️ Your expenses exceed your income! Consider revising your budget.")
    elif disposable_income < income * 0.2:
        st.warning("⚠️ Your savings are less than 20% of your income. Aim to save more!")
    else:
        st.success("✅ Great job! You're saving a healthy portion of your income.")


    st.write("Budget analysis complete.")