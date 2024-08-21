import random

class SavingSafari:
    def __init__(self, income, saving, duration):
        self.income = income
        self.savings = saving
        self.gameduration = duration
        self.current_month = 0
        self.emergency_fund_goal = income * 3
        self.vacation_fund_goal = income * 2
        self.big_purchase_goal = income * 12
        self.goals_achieved = {"emergency_fund": False, "vacation_fund": False, "big_purchase": False}

    def allocate_funds(self):
        while True:
            try:
                expenses = float(input("Enter amount for expenses: "))
                savings = float(input("Enter amount for savings: "))
                wants = float(input("Enter amount for wants: "))
                
                if expenses + savings + wants > self.income:
                    print("Total allocation exceeds monthly income. Please try again.")
                else:
                    return expenses, savings, wants
            except ValueError:
                print("Please enter valid numbers.")

    def random_event(self):
        event = random.choice(["expense", "windfall", "none"])
        amount = random.randint(100, 1000)
        
        if event == "expense":
            print(f"Unexpected expense of ${amount}!")
            self.savings -= amount
        elif event == "windfall":
            print(f"Windfall of ${amount}!")
            self.savings += amount

    def apply_interest(self):
        interest_rate = 0.005  # 0.5% monthly interest
        interest = self.savings * interest_rate
        self.savings += interest
        print(f"Interest earned: ${interest:.2f}")

    def check_goals(self):
        
        if self.savings >= self.vacation_fund_goal and not self.goals_achieved["vacation_fund"]:
            print("Congratulations! You've reached your vacation fund goal!")
            self.goals_achieved["vacation_fund"] = True

        if self.savings >= self.emergency_fund_goal and not self.goals_achieved["emergency_fund"]:
            print("Congratulations! You've reached your emergency fund goal!")
            self.goals_achieved["emergency_fund"] = True
        
        if self.savings >= self.big_purchase_goal and not self.goals_achieved["big_purchase"]:
            print("Congratulations! You've reached your big purchase goal!")
            self.goals_achieved["big_purchase"] = True

    def play(self):
        print("Welcome to Saving Safari!")
        print(f"Your monthly income is ${self.income}")
        print(f"Your initial savings balance is ${self.savings}")
        print(f"Game duration: {self.gameduration} months")
        print("Goals:")
        print(f"1. Emergency Fund: ${self.emergency_fund_goal}")
        print(f"2. Vacation Fund: ${self.vacation_fund_goal}")
        print(f"3. Big Purchase: ${self.big_purchase_goal}")

        while self.current_month < self.gameduration:
            self.current_month += 1
            print(f"\nMonth {self.current_month}")
            expenses, savings, wants = self.allocate_funds()
            self.savings += savings
            self.random_event()
            self.apply_interest()
            self.check_goals()
            print(f"Current savings: ${self.savings:.2f}")

        print("\nGame Over!")
        print(f"Final savings: ${self.savings:.2f}")
        print("Goals achieved:")
        for goal, achieved in self.goals_achieved.items():
            print(f"{goal.replace('_', ' ').title()}: {'Yes' if achieved else 'No'}")




game = SavingSafari(income=3000, saving=1000, duration=24)
game.play()