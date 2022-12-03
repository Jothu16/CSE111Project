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

<h2>HTML Forms</h2>

<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form> 

<p>"/action_page.php".</p>

</body>
</html>