function showMessage(type, message) {
    const warningDiv = document.getElementById('warning');
    const successDiv = document.getElementById('success');
    
    
    // Select which div to use
    let div;
    if (type === 'warning') {
        div = warningDiv;
    } else if (type === 'success') {
        div = successDiv;
    } else {
        alert('Unknown message type: ' + message);
        return;
    }
    
    // Set the message
    div.querySelector('.message').textContent = message;
    
    // Make it visible with a small delay to ensure the display property is set
    div.style.display = 'block';
    
    // Hide it after 3 seconds
    setTimeout(() => {
            div.style.display = 'none';
    }, 3000);
}