document.addEventListener("DOMContentLoaded", function () {
    let countrySelect = document.getElementById("id_country");

    if (countrySelect) {
        let countrySelected = countrySelect.value;
        
        // Apply grey color if no country is selected
        if (!countrySelected) {
            countrySelect.style.color = "#aab7c4";
        }

        // Change color when user selects a country
        countrySelect.addEventListener("change", function () {
            countrySelected = this.value;
            if (!countrySelected) {
                this.style.color = "#aab7c4";
            } else {
                this.style.color = "#000";
            }
        });
    }
});
