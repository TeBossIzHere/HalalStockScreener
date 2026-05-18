// Halal Stock Screener — client-side logic.
// Calculations were previously done server-side in Flask (app.py); ported here
// so the app can deploy as a fully static site on Netlify.

document.addEventListener("DOMContentLoaded", function () {
    const popupOverlay = document.getElementById("popup-overlay");
    const closePopupButton = document.getElementById("close-popup-button");

    if (popupOverlay) {
        popupOverlay.style.display = "flex";
    }
    if (closePopupButton) {
        closePopupButton.addEventListener("click", function () {
            popupOverlay.style.display = "none";
        });
    }

    // Expandable info sections
    document.querySelectorAll(".expand-button").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.dataset.target;
            const targetSection = document.getElementById(targetId);
            const isAlreadyOpen = targetSection.style.display === "block";

            document.querySelectorAll(".expand-section").forEach(section => {
                section.style.display = "none";
            });
            if (!isAlreadyOpen) {
                targetSection.style.display = "block";
            }
        });
    });

    // Form submission — compute ratios client-side
    const form = document.getElementById("screener-form");
    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            runScreening();
        });
    }
});

function safeFloat(value) {
    if (value === null || value === undefined) return null;
    const cleaned = String(value).trim().replace(/,/g, "").replace(/\$/g, "");
    if (cleaned === "") return null;
    const num = Number(cleaned);
    return Number.isFinite(num) ? num : null;
}

function runScreening() {
    const errorEl = document.getElementById("error-message");
    const resultsEl = document.getElementById("results-container");

    errorEl.style.display = "none";
    errorEl.textContent = "";

    const mv = safeFloat(document.getElementById("mv").value);
    const tr = safeFloat(document.getElementById("tr").value);
    const ar = safeFloat(document.getElementById("ar").value);
    const debt = safeFloat(document.getElementById("debt").value);
    const cash = safeFloat(document.getElementById("cash").value);
    const ibs = safeFloat(document.getElementById("ibs").value);
    const hr = safeFloat(document.getElementById("hr").value);

    if ([mv, tr, ar, debt, cash, ibs, hr].some(v => v === null)) {
        errorEl.textContent = "Missing or Invalid input. Please fill all sections with numeric values.";
        errorEl.style.display = "block";
        resultsEl.style.display = "none";
        return;
    }

    const arRatio = mv ? (ar / mv) * 100 : 0;
    const debtRatio = mv ? (debt / mv) * 100 : 0;
    const liquidRatio = mv ? ((cash + ibs) / mv) * 100 : 0;
    const haramRatio = tr ? (hr / tr) * 100 : 0;

    setResult("ar-result", "Accounts Receivable Ratio", arRatio, 49);
    setResult("debt-result", "Debt Ratio", debtRatio, 33);
    setResult("liquid-result", "Liquid Assets Ratio", liquidRatio, 33);
    setResult("haram-result", "Haram Revenue Ratio", haramRatio, 5);

    resultsEl.style.display = "block";
}

function setResult(elementId, label, ratio, threshold) {
    const el = document.getElementById(elementId);
    const status = ratio <= threshold ? "compliant" : "non-compliant";
    el.textContent = `${label}: ${ratio.toFixed(2)}% (${status})`;
    el.classList.remove("compliant", "non-compliant");
    el.classList.add(status);
}
