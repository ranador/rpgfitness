function dragOverHandler(ev) {
    console.log('File(s) in drop zone');
    ev.preventDefault();
}

function dropHandler(ev) {
    ev.preventDefault();
    
    // Get the file input element and status div
    const fileInput = document.getElementById('file-input');
    const form = document.getElementById('upload-form');
    
    function log(message) {
        console.log(message);
    }
    
    if (ev.dataTransfer.files) {
        // Create FormData
        const formData = new FormData(form);
        
        // Remove any existing files from the FormData
        formData.delete('files');
        
        // Add each dropped file
        [...ev.dataTransfer.files].forEach(file => {
            formData.append('files', file);
        });
        
        // Get CSRF token
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        // Submit using fetch
        fetch(form.action || window.location.href, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {
            // Replace the current page content with the response
            document.documentElement.innerHTML = html;
        })
        .catch(error => {
            log('Error: ' + error.message);
        });
    }
}