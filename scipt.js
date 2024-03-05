// Vehicle data (replace with your actual data)
const vehiclesData = [
    { name: "Truck", images: ["truck1.jpg", "truck2.jpg"], capacity: "10 tons", rentalRate: "$100/day" },
    { name: "Van", images: ["van1.jpg", "van2.jpg"], capacity: "6 passengers", rentalRate: "$80/day" }
    // Add more vehicles here
];

// Function to generate HTML for vehicles
function generateVehicleHTML(vehicle) {
    let imagesHTML = "";
    vehicle.images.forEach(image => {
        imagesHTML += `<img src="${image}" alt="${vehicle.name}">`;
    });

    return `
        <div class="vehicle">
            ${imagesHTML}
            <h3>${vehicle.name}</h3>
            <p>Capacity: ${vehicle.capacity}</p>
            <p>Rental Rate: ${vehicle.rentalRate}</p>
            <button>Book Now</button>
        </div>
    `;
}

// Function to display vehicles
function displayVehicles() {
    const vehicleContainer = document.getElementById("vehicle-container");
    vehicleContainer.innerHTML = ""; // Clear existing content

    vehiclesData.forEach(vehicle => {
        const vehicleHTML = generateVehicleHTML(vehicle);
        vehicleContainer.innerHTML += vehicleHTML;
    });
}

// Display vehicles when the page loads
displayVehicles();
