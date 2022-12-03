<?php

$pdo = new PDO('sqlite:newdb.db');

$statement = $pdo->query("SELECT * FROM Users");

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

var_dump($rows);