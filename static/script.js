document.addEventListener("DOMContentLoaded", function () {
    const popupOverlay = document.getElementById("popup-overlay");
    const closePopupButton = document.getElementById("close-popup-button");

    // 🚀 Only show pop-up if results are NOT displayed (prevents showing after submission)
    const resultsContainer = document.querySelector(".results-container");

    if (popupOverlay && !resultsContainer) {
        popupOverlay.style.display = "flex"; // ✅ Ensure it only shows on fresh loads
        console.log("Pop-up should be visible now.");
    }

    if (closePopupButton) {
        closePopupButton.addEventListener("click", function () {
            popupOverlay.style.display = "none";
        });
    }
});

function closePopup() {
    document.getElementById("popup-overlay").style.display = "none";
}

function toggleExpand(id) {
    let section = document.getElementById(id);
    section.style.display = section.style.display === "none" ? "block" : "none";
}

document.addEventListener("DOMContentLoaded", function () {
    let expandButtons = document.querySelectorAll(".expand-button");

    expandButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent form validation issue

            let targetId = this.dataset.target;
            let targetSection = document.getElementById(targetId);
            let isAlreadyOpen = targetSection.style.display === "block";

            // Close all sections before opening the selected one
            document.querySelectorAll(".expand-section").forEach(section => {
                section.style.display = "none";
            });

            // Toggle visibility of the selected section
            if (!isAlreadyOpen) {
                targetSection.style.display = "block";
            }
        });
    });

    // Debugging pop-up display state
    console.log("Final Pop-up Display State:", document.getElementById("popup-overlay")?.style.display);
});

document.addEventListener("DOMContentLoaded", function () {
    // ✅ Only reset the page on actual refresh, NOT after submission
    if (!sessionStorage.getItem("pageReloaded")) {
        sessionStorage.setItem("pageReloaded", "true");  // ✅ Track refresh state

        sessionStorage.removeItem("popupClosed");  // ✅ Ensure pop-up reappears
        sessionStorage.removeItem("submittedData"); // ✅ Clears previous form data

        let form = document.querySelector("form");
        if (form) {
            form.reset();  // ✅ Clears input fields on refresh only
        }

        const popupOverlay = document.getElementById("popup-overlay");
        if (popupOverlay) {
            popupOverlay.style.display = "flex";  // ✅ Shows pop-up only on fresh loads
        }

        let resultsContainer = document.querySelector(".results-container");
        if (resultsContainer) {
            resultsContainer.style.display = "none"; // ✅ Hide results on refresh
        }
    } else {
        sessionStorage.removeItem("pageReloaded");  // ✅ Prevents looping refresh behavior
    }

    // ✅ Fix: Prevent auto-refresh after submit
    let submitButton = document.querySelector("button[type='submit']");
    if (submitButton) {
        submitButton.addEventListener("click", function (event) {
            event.preventDefault();  // ✅ Stops form submission from triggering an immediate page reload
            document.querySelector("form").submit();  // ✅ Allows normal submission without auto-refresh
        });
    }
});