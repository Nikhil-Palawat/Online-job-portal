
/* static/js/main.js */
document.addEventListener('DOMContentLoaded', function() {
    // Job search form handling
    const searchForm = document.querySelector('.search-box form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const query = this.querySelector('input[name="q"]').value;
            const location = this.querySelector('input[name="location"]').value;
            
            window.location.href = `/jobs?q=${encodeURIComponent(query)}&location=${encodeURIComponent(location)}`;
        });
    }

    // Job application form handling
    const applicationForm = document.querySelector('.application-form');
    if (applicationForm) {
        applicationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Application submitted successfully!');
                    window.location.reload();
                } else {
                    alert('Error submitting application. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        });
    }
});
