<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abike Logistics</title>
    <style>
        body {
            background-color: red;
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: black;
            padding: 20px 0;
            text-align: center;
        }

        nav ul {
            list-style-type: none;
            padding: 0;
        }

        nav ul li {
            display: inline;
            margin-right: 20px;
        }

        nav ul li a {
            text-decoration: none;
            color: white;
        }

        section {
            padding: 20px;
        }

        .catalog {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .vehicle {
            width: 300px;
            margin: 20px;
            background-color: #333;
            padding: 20px;
            border-radius: 10px;
        }

        .vehicle img {
            width: 100%;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        footer {
            background-color: red;
            color: white;
            padding: 20px 0;
            text-align: center;
        }
    </style>
</head>
<body>
<header>
    <h1>Abike Integrated ventures Logistics limited</h1>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#catalog">Catalog</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</header>
<section id="home">
    <h2>Welcome to Abike Integrated ventures Logistics limited</h2>
    <p>Rent top-quality vehicles for your logistics needs.</p>
</section>
<section id="catalog">
    <h2>Vehicle Catalog</h2>
    <div class="catalog">
        <div class="vehicle">
            <img src="truck1.jpg" alt="Truck 1">
            <h3>hilux</h3>
            <p>Model: Toyota </p>
            <p>Rental Rate: #75,000/day</p>
            <button onclick="window.location.href='contact.html'">Book Now</button>
        </div>
        <div class="vehicle">
            <img src="truck2.jpg" alt="Truck 2">
            <h3>vaccum truck</h3>
            <p>Capacity: 8 tons</p>
            <p>Rental Rate: #90,000/day</p>
            <button onclick="window.location.href='contact.html'">Book Now</button>
        </div>
        <div class="vehicle">
            <img src="car1.jpg" alt="toyota fortuner">
            <h3>Fortuner </h3>
            <p>Model: Toyota ></p>
            <p>Rental Rate: #50,000/day</p>
            <button onclick="window.location.href='contact.html'">Book Now</button>
        </div>
        <div class="vehicle">
            <img src="car2.jpg" alt="Car 2">
            <h3>Firetruck </h3>
            <p>Model: fire truck</p>
            <p>Rental Rate: #100,000/day</p>
            <button onclick="window.location.href='contact.html'">Book Now</button>
        </div>
        <div class="vehicle">
            <img src="car3.jpg" alt="Car 3">
            <h3>Toyota coaster </h3>
            <p>Model: fire truck</p>
            <p>Rental Rate: #120,000/day</p>
            <button onclick="window.location.href='contact.html'">Book Now</button>
        </div>
        <!-- Add more vehicles here -->
    </div>
</section>
<footer id="contact">
    <h2>Contact Us</h2>
    <p>Phone: +2347035260938</p>
    <p>Email: abikeintegratedventures@yahoo.com</p>
    <p>Address: 581 Ikwerre Road, Rumigbo, Rivers State, Port Harcourt, Nigeria</p>
    <!-- Contact form -->
    <form action="/send_email" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br>
        <input type="submit" value="Submit">
    </form>
</footer>
</body>
</html>

