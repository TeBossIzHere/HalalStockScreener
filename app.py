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
# git push origin main (or your feature branch).
# ...

# - Accounts Receivable / Market Value of Equity (36-month average) < 49%
# - Debt / Market Capitalization of Equity (36-month average) < 33%
# - (Cash + Interest-Bearing Securities) / Market Value of Equity (36-month average) < 33%
# - Revenue from haram sources < 5% of total revenue.

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for using sessions

# Helper functions
def clean_int(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return int(value)
    try:
        return int(value.replace(",", ""))
    except ValueError:
        return None

def account_receivable_benchmark(ar, mv):
    ar = clean_int(ar)
    mv = clean_int(mv)
    if ar is None or mv is None or mv == 0:
        return "Invalid input for Account Receivable Benchmark."
    percentage = ar / mv * 100
    result = "PASSED" if percentage <= 49 else "FAILED"
    return f"Account Receivable Benchmark: {result}, currently: {round(percentage, 2)}%."

def debt_benchmark(debt, mv):
    debt = clean_int(debt)
    mv = clean_int(mv)
    if debt is None or mv is None or mv == 0:
        return "Invalid input for Debt-to-Value Benchmark."
    percentage = debt / mv * 100
    result = "PASSED" if percentage <= 33 else "FAILED"
    return f"Debt-to-Value Benchmark: {result}, currently: {round(percentage, 2)}%."

def liquid_asset_benchmark(cash, ibs, mv):
    cash = clean_int(cash)
    ibs = clean_int(ibs)
    mv = clean_int(mv)
    if cash is None or ibs is None or mv is None or mv == 0:
        return "Invalid input for Liquid Asset Benchmark."
    percentage = (cash + ibs) / mv * 100
    result = "PASSED" if percentage <= 33 else "FAILED"
    return f"Liquid Asset Benchmark: {result}, currently: {round(percentage, 2)}%."

def revenue_from_haram_benchmark(hr, tr):
    hr = clean_int(hr)
    tr = clean_int(tr)
    if hr is None or tr is None or tr == 0:
        return "Invalid input for Revenue-from-Haram Benchmark."
    percentage = hr / tr * 100
    result = "PASSED" if percentage <= 5 else "FAILED"
    return f"Revenue-from-Haram Benchmark: {result}, currently: {round(percentage, 2)}%."

def safe_convert(value):
    if isinstance(value, str):
        try:
            return float(value.replace(",", ""))
        except ValueError:
            return None
    elif isinstance(value, (int, float)):
        return value
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # process the form
        mv = safe_convert(request.form.get('mv', ''))
        tr = safe_convert(request.form.get('tr', ''))
        ar = safe_convert(request.form.get('ar', ''))
        debt = safe_convert(request.form.get('debt', ''))
        cash = safe_convert(request.form.get('cash', ''))
        ibs = safe_convert(request.form.get('ibs', ''))
        hr = safe_convert(request.form.get('hr', ''))

        if None in [mv, tr, ar, debt, cash, ibs, hr]:
            session['error_message'] = "Invalid input: Please ensure all values are numeric."
        else:
            session['error_message'] = None
            session['ar_result'] = account_receivable_benchmark(ar, mv)
            session['debt_result'] = debt_benchmark(debt, mv)
            session['liquid_result'] = liquid_asset_benchmark(cash, ibs, mv)
            session['haram_result'] = revenue_from_haram_benchmark(hr, tr)

        # After handling the POST, REDIRECT to GET (important!)
        return redirect(url_for('index'))

    # If GET request
    ar_result = session.pop('ar_result', None)
    debt_result = session.pop('debt_result', None)
    liquid_result = session.pop('liquid_result', None)
    haram_result = session.pop('haram_result', None)
    error_message = session.pop('error_message', None)

    # Display results only if they exist
    results_display = any([ar_result, debt_result, liquid_result, haram_result])

    return render_template('index.html',
                            error_message=error_message,
                            ar_result=ar_result,
                            debt_result=debt_result,
                            liquid_result=liquid_result,
                            haram_result=haram_result,
                            results_display=results_display)

if __name__ == '__main__':
    app.run(debug=True)
