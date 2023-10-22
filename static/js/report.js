// Get elements
const reportLink = document.getElementById("report-link");
const reportModal = document.getElementById("report-modal");
const closeBtn = document.getElementById("close-modal");
const submitReportBtn = document.getElementById("submit-report");
const reportSuccessMessage = document.getElementById("report-success-message");

// Show the report modal when the "Report Photo" link is clicked
reportLink.addEventListener("click", function(event) {
    event.preventDefault();
    reportModal.style.display = "block";
});

// Close the report modal when the "Close" button is clicked
closeBtn.addEventListener("click", function() {
    reportModal.style.display = "none";
    reportSuccessMessage.textContent = "";
});

// Handle the reporting process when the "Report" button is clicked
submitReportBtn.addEventListener("click", function () {
    reportSuccessMessage.textContent = "Report received. Admin will review and follow up.";
});

// Close the report modal when the background is clicked
window.addEventListener("click", function(event) {
    if (event.target === reportModal) {
        reportModal.style.display = "none";
        reportSuccessMessage.textContent = "";
    }
});
