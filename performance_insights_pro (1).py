# =====================================================
# Performance Insights Pro - Sales Goal Analyzer
# Created by Donovan Parrish - 2025
# =====================================================

def sales_performance_tracker():
    print("="*55)
    print("   PERFORMANCE INSIGHTS PRO - SALES GOAL ANALYZER")
    print("="*55)
    print("A quick tool to measure sales performance vs. goals")
    print()

    # Input values
    target = int(input("Enter your sales goal: "))
    actual = int(input("Enter your actual sales achieved: "))

    # Calculate performance
    performance = ((actual - target) / target) * 100

    print("\n--- Performance Report ---")
    print(f"Sales Goal: {target}")
    print(f"Actual Sales: {actual}")

    if performance > 0:
        print(f"Performance: {performance:.2f}% over target")
        print("Status: EXCEEDED GOAL ✅")
    elif performance == 0:
        print("Performance: 0.00% (Met Goal)")
        print("Status: MET GOAL ✔")
    else:
        print(f"Performance: {abs(performance):.2f}% below target")
        print("Status: BELOW GOAL ❌")

    print("="*55)

sales_performance_tracker()
