<?php

$pdo = new PDO('sqlite:newdb.db');

$statement = $pdo->query("SELECT * FROM newdb");

$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

var_dump($rows);