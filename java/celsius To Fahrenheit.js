<!DOCTYPE html>
<html>
<head>
    <title>Celsius to Fahrenheit Converter</title>
</head>
<body>

    <h2>Celsius to Fahrenheit Converter</h2>

    <label for="celsius">Enter temperature in Celsius:</label>
    <input type="number" id="celsius" placeholder="Celsius">

    <button onclick="convertToFahrenheit()">Convert</button>

    <p id="result"></p>

    <script>
        function convertToFahrenheit() {
            var celsius = document.getElementById("celsius").value;
            var fahrenheit = (celsius * 9/5) + 32;
            document.getElementById("result").innerHTML = celsius + "°C is equal to " + fahrenheit.toFixed(2) + "°F";
        }
    </script>

</body>
</html>
