# Daily Git To-Do List
# Start:
#
# git pull origin main (or your feature branch)
#
# Work:
#
# git status (to check changes)
#
# git add . (or git add <file> for specific files)
#
# Commit:
#
# git commit -m "Your descriptive message"
#
# End:
#
# git push origin main (or your feature branch)
# ...

# - Accounts Receivable / Market Value of Equity (36-month average) < 49%
# - Debt / Market Capitalization of Equity (36-month average) < 33%
# - (Cash + Interest-Bearing Securities) / Market Value of Equity (36-month average) < 33%
# - Revenue from haram sources < 5% of total revenue.

def accountReceivableBenchmark(AR, MV):
    ARBenchmarkPercentage = int(str(AR).replace(",", "")) / int(str(MV).replace(",", "")) * 100
    if ARBenchmarkPercentage <= 49:
        print("Account Receivable Benchmark: PASSED, currently: " + str(round(ARBenchmarkPercentage, 2)) + "%.")
    else:
        print("Account Receivable Benchmark: FAILED, currently: " + str(round(ARBenchmarkPercentage, 2)) + "%.")

def debtBenchmark(D, MV):
    debtBenchmarkPercentage = int(str(D).replace(",", "")) / int(str(MV).replace(",", "")) * 100
    if debtBenchmarkPercentage <= 33:
        print("Debt-to-Value Benchmark: PASSED, currently: " + str(round(debtBenchmarkPercentage, 2)) + "%.")
    else:
        print("Debt-to-Value Benchmark: FAILED, currently: " + str(round(debtBenchmarkPercentage, 2)) + "%.")

def liquidAssetBenchmark(C, IBS, MV):
    liquidAssetBenchmark = (int(str(C).replace(",", "")) + int(str(IBS).replace(",", ""))) / int(str(MV).replace(",", "")) * 100
    if liquidAssetBenchmark <= 33:
        print("Liquid Asset Benchmark: PASSED, currently: " + str(round(liquidAssetBenchmark, 2)) + "%.")
    else:
        print("Liquid Asset Benchmark: FAILED, currently: " + str(round(liquidAssetBenchmark, 2)) + "%.")

def revenueFromHaramBenchmark(HR, TR):
    revenueFromHaramBenchMarkPercentage = int(str(HR).replace(",", "")) / int(str(TR).replace(",", "")) * 100
    if revenueFromHaramBenchMarkPercentage <= 5:
        print("Revenue-from-Haram Benchmark: PASSED, currently: " + str(round(revenueFromHaramBenchMarkPercentage, 2)) + "%.")
    else:
        print("Revenue-from-Haram Benchmark: FAILED, currently: " + str(round(revenueFromHaramBenchMarkPercentage, 2)) + "%.")

MV = input("What is the Market Value of the Equity?   ")
TR = input("What is Total Revenue of the Equity?   ")
AR = input("What is the accounts receivable?   ")
D = input("What is the Debt of the Equity?   ")
C = input("What is the Total Cash and Cash Equivalents (i.e Gold, Bitcoin, etc.)   ")
IBS = input("What is the Total Value of Interest-Bearing Securities (i.e Bonds, Treasuries)?   ")
HR = input("What is the Total Revenue from Haram Sources of the Equity?   ")



accountReceivableBenchmark(AR, MV)
debtBenchmark(D, MV)
liquidAssetBenchmark(C, IBS, MV)
revenueFromHaramBenchmark(HR, TR)