# JavaScript code block that handles the toggling of the register button
# based on the state of the privacy policy checkbox, and includes a redirect
# function for successful registration.

js_code = """
// Function to toggle the register button based on checkbox state
function toggleRegisterButton() {
    document.getElementById('register-btn').disabled = !document.getElementById('privacy_policy').checked;
}

// Run the toggle function on page load to disable the button initially if checkbox is not checked
document.addEventListener('DOMContentLoaded', function() {
    toggleRegisterButton();  // Ensure initial state
});

// Add event listener for changes in the checkbox state
document.getElementById('privacy_policy').addEventListener('change', function() {
    toggleRegisterButton();  // Update button state when checkbox changes
});

// Function to redirect to the sign-in page after successful registration
function redirectToSignIn() {
    setTimeout(function() {
        window.location.href = '/sign-in-page';
    }, 3000); // 3-second delay before redirect
}
"""

def sign_up_js_scripts():
    """
    Returns the JavaScript code required for the sign-up page.

    The returned JavaScript includes:
    - A function to enable or disable the 'Register' button based on whether the 
      'Privacy Policy' checkbox is checked.
    - Event listeners that handle the initial state of the checkbox and detect 
      changes to update the button state.
    - A function to redirect to the sign-in page with a 3-second delay after a 
      successful registration.

    Returns:
        str: The JavaScript code as a string.
    """
    return js_code  # Return the JavaScript code as a string
