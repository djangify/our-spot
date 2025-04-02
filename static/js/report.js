// This script handles the reporting functionality for the web application.
document.addEventListener('DOMContentLoaded', function () {
    const reportLink = document.getElementById('report-link');
    const reportModal = document.getElementById('report-modal');
    const closeModal = document.getElementById('close-modal');
    const cancelReport = document.getElementById('cancel-report');
    const reportForm = document.getElementById('report-form');
    const successMessage = document.getElementById('report-success-message');

    function showModal() {
        reportModal.classList.remove('hidden');
        reportModal.classList.add('flex', 'items-center', 'justify-center');
    }

    function hideModal() {
        reportModal.classList.add('hidden');
        reportModal.classList.remove('flex', 'items-center', 'justify-center');
    }

    reportLink.addEventListener('click', showModal);
    closeModal.addEventListener('click', hideModal);
    cancelReport.addEventListener('click', hideModal);

    // Close modal when clicking outside of it
    reportModal.addEventListener('click', function (event) {
        if (event.target === reportModal) {
            hideModal();
        }
    });

    // Handle form submission via AJAX
    reportForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(reportForm);
        fetch(reportForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
            .then(response => response.json())
            .then(data => {
                hideModal();
                successMessage.textContent = data.message;
                setTimeout(() => {
                    successMessage.textContent = '';
                }, 5000);
            })
            .catch(error => {
                console.error('Error:', error);
                hideModal();
                successMessage.textContent = 'There was an error submitting your report. Please try again.';
                setTimeout(() => {
                    successMessage.textContent = '';
                }, 5000);
            });
    });
});
