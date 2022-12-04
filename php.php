<?php

$pdo = new PDO('sqlite:newdb.db');

$statement = $pdo->query("SELECT * FROM Users");

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

var_dump($rows);

$statement = $pdo->query("SELECT * FROM Continent");

echo "<br>";
echo "<br>";

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

var_dump($rows);

$statement = $pdo->query("SELECT * FROM Country");

echo "<br>";
echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM Capital_City");

echo "<br>";
echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM History");

echo "<br>";
echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM Status");

echo "<br>";
echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM UserEdits");

echo "<br>";
echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

$statement = $pdo->query("SELECT * FROM HistoryStatus");

echo "<br>";
echo "<br>";

var_dump($rows);

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

echo "<br>";
echo "<br>";

var_dump($rows);

?>