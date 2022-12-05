<?php
    function deletecity($city) {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "DELETE FROM Capital_City WHERE Capital_City.Name = '" . $city. "'";

        echo "<table>";
                echo "<caption>Capital City</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>City Key</th><th>Country Key</th><th>Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

        $db->query($sql);

        $ret = $db->query("select * from Capital_City");
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["City_Key"] . "</td>" .
                "<td>" . $row["Country_Key"] . "</td>" .
                "<td>" . $row["Name"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    deletecity($_POST["city_name"]);

?>