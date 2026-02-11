class AdvancedWealthSimulator(WealthSimulator):
    def __init__(self, monthly_income, saving_rate, annual_return, salary_growth, years):
        super().__init__(monthly_income, saving_rate, annual_return, years)
        self.salary_growth = salary_growth

    def simulate(self):
        data = []
        monthly_return = self.annual_return / 12
        current_salary = self.monthly_income
        
        for year in range(1, self.years + 1):
            for month in range(12):
                saving = current_salary * self.saving_rate
                self.wealth = self.wealth * (1 + monthly_return) + saving
            
            # gaji naik tiap tahun
            current_salary *= (1 + self.salary_growth)
            
            data.append({
                "Year": year,
                "Wealth": round(self.wealth, 2),
                "Monthly Salary": round(current_salary, 2)
            })
        
        return pd.DataFrame(data)

sim2 = AdvancedWealthSimulator(
    monthly_income=8_000_000,
    saving_rate=0.3,
    annual_return=0.10,
    salary_growth=0.05,  # gaji naik 5% per tahun
    years=20
)

df2 = sim2.simulate()
print(df2)
