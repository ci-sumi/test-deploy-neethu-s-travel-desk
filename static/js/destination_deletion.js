
    // Function to open the confirmation modal
    function openModal() {
        document.getElementById("deleteModal").style.display = "flex";
        document.body.classList.add("no-scroll");
    }

    // Function to close the confirmation modal
    function closeModal() {
        document.getElementById("deleteModal").style.display = "none";
        document.body.classList.remove("no-scroll");
    }