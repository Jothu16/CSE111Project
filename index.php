<?php

$pdo = new PDO('sqlite:newdb.db');

$statement = $pdo->query("SELECT * FROM Users");

echo "<br>";

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

var_dump($rows);

$statement = $pdo->query("SELECT * FROM Continent");

echo "<br>";

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

var_dump($rows);

$statement = $pdo->query("SELECT * FROM Country");

echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM Capital_City");

echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM History");

echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM Status");

echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM UserEdits");

echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM HistoryStatus");

echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

echo "<br>";

var_dump($rows);

?>

<html>
<body>

<button onclick="myFunction()">count amount of history entries and user entries</button>

<button onclick="myFunction()">count the amount of countries and their capital cities and their entries(city count = country count since country can only have 1 capital)</button>

<button onclick="myFunction()">get current userkey</button>

<button onclick="myFunction()">add new user - copy paste this and change variables to make work with other tables</button>

<button onclick="myFunction()">delete user</button>

<button onclick="myFunction()">add new country</button>

<button onclick="myFunction()">add new city</button>

<button onclick="myFunction()">delete country</button>

<button onclick="myFunction()">delete city</button>

<button onclick="myFunction()">Delete data relating to a city - copy paste this segment and change some names to make work with other tables</button>

<button onclick="myFunction()">Update file - date = new_date where date = old_date</button>

<button onclick="myFunction()">update aqi value of a city - records user who did - check valid data later</button>

<button onclick="myFunction()">update history with new entry</button>

<button onclick="myFunction()">add new entry to current aq database</button>

<button onclick="myFunction()">Select statment get data from Current_AQ_Info</button>

<button onclick="myFunction()">count all edits made by users today form lowest to highest</button>

<button onclick="myFunction()">print lowest and highest country's AQI Value</button>

<button onclick="myFunction()">print all cities with a "good" status</button>

<button onclick="myFunction()">print all countries with a "good" status</button>

<button onclick="myFunction()">print all continents with a country with "good" status and how many</button>

<button onclick="myFunction()">Count the amount of entries for each status description</button>

<button onclick="myFunction()">Print the history of a city</button>

<button onclick="myFunction()">print average air quality and the average status of each continent</button>

<button onclick="myFunction()">Print the history of a city</button>

<button onclick="myFunction()">count the amount of times each city had a certain status</button>

<button onclick="myFunction()">find cities that had both "Good" and "Moderate" Statuses in its history - change variables if needed</button>

<button onclick="myFunction()">find all cities except for unhealthy or worse cities</button>

<button onclick="myFunction()">print all cities that had changes in statuses and order by date</button>

<button onclick="myFunction()"># select all countries status</button>

</body>
</html>