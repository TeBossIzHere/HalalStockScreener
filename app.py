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

from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)

app.config["SECRET_KEY"] = "your_unique_secret_key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        session.clear()

    error_message = None
    results_display = False
    ar_result, debt_result, liquid_result, haram_result = "", "", "", ""

    if request.method == "POST":
        session["submitted"] = True

        try:
            def safe_float(value):
                value = value.strip().replace(",", "").replace("$", "")
                return float(value) if value and value.replace(".", "").isdigit() else None

            mv = safe_float(request.form.get("mv", ""))
            tr = safe_float(request.form.get("tr", ""))
            ar = safe_float(request.form.get("ar", ""))
            debt = safe_float(request.form.get("debt", ""))
            cash = safe_float(request.form.get("cash", ""))
            ibs = safe_float(request.form.get("ibs", ""))
            hr = safe_float(request.form.get("hr", ""))

            if None in [mv, tr, ar, debt, cash, ibs, hr]:
                raise ValueError("Missing or Invalid input. Please fill all sections with numeric values.")

            ar_ratio = (ar / mv) * 100 if mv else 0
            debt_ratio = (debt / mv) * 100 if mv else 0
            liquid_ratio = ((cash + ibs) / mv) * 100 if mv else 0
            haram_ratio = (hr / tr) * 100 if tr else 0

            ar_status = "compliant" if ar_ratio <= 33 else "non-compliant"
            debt_status = "compliant" if debt_ratio <= 33 else "non-compliant"
            liquid_status = "compliant" if liquid_ratio <= 33 else "non-compliant"
            haram_status = "compliant" if haram_ratio <= 5 else "non-compliant"

            ar_result = f"Accounts Receivable Ratio: {ar_ratio:.2f}% ({ar_status})"
            debt_result = f"Debt Ratio: {debt_ratio:.2f}% ({debt_status})"
            liquid_result = f"Liquid Assets Ratio: {liquid_ratio:.2f}% ({liquid_status})"
            haram_result = f"Haram Revenue Ratio: {haram_ratio:.2f}% ({haram_status})"

            results_display = True
        except ValueError:
            error_message = "Missing or Invalid input. Please fill all sections with numeric values."

    return render_template("index.html", show_popup="submitted" not in session, error_message=error_message,
                           results_display=results_display, ar_result=ar_result, debt_result=debt_result,
                           liquid_result=liquid_result, haram_result=haram_result)

if __name__ == "__main__":
    app.run(debug=True)
