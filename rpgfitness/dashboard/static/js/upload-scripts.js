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
    
    // Define allowed file types
    const allowedTypes = ['.csv'];  // add or remove types as needed
    
    if (ev.dataTransfer.files) {
        // Check if all files are of allowed type
        const files = [...ev.dataTransfer.files];
        const invalidFiles = files.filter(file => !allowedTypes.includes(file.type));
        
        if (invalidFiles.length > 0) {
            // If there are invalid files, show error and return
            const invalidTypes = invalidFiles.map(file => file.type || 'unknown type').join(', ');
            showMessage('warning',`Invalid file type(s): ${invalidTypes}\nAllowed types are: ${allowedTypes.join(', ')}`);
            return;
        }
        
        // Create FormData
        const formData = new FormData(form);
        
        // Remove any existing files from the FormData
        formData.delete('files');
        
        // Add each dropped file
        files.forEach(file => {
            formData.append('files', file);
        });
        
        // Get CSRF token
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        // Optional: Add loading state
        const dropZone = document.getElementById('drop-zone');
        dropZone.classList.add('uploading');
        
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
            showMessage('warning', 'An error occurred while uploading the file(s).' + error.message);
        })
        .finally(() => {
            // Remove loading state
            dropZone.classList.remove('uploading');
        });
    }
}