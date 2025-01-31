/* jshint esversion: 6 */
/* exported openClearModal, clearForm */
// Function to open the clear confirmation modal
function openClearModal() {
    document.getElementById("clearModal").style.display = "flex";
}

// Function to close the clear confirmation modal
function closeClearModal() {
    document.getElementById("clearModal").style.display = "none";
}

// Function to clear form fields and close the modal
function clearForm() {
    // Get the form element
    const form = document.getElementById("budget-form");
    
    // Reset all input fields
    form.reset();  // Reset all form fields (this works for most inputs)

    // Clear the values for any number inputs explicitly
    const numberInputs = form.querySelectorAll('input[type="number"]');
    numberInputs.forEach(input => {
        input.value = ''; // Explicitly clear number inputs
    });

    // Clear any select dropdowns (destination is a select element)
    const selectInputs = form.querySelectorAll('select');
    selectInputs.forEach(select => {
        select.selectedIndex = 0; // Reset the select dropdown to no selection
    });

    const totalCostAlert = document.querySelector(".alert-success");
    if (totalCostAlert) {
        totalCostAlert.style.display = "none"; // Hide the total cost alert after clearing
    }

    // Close the modal
    closeClearModal();
}
