<?php
    function addnewcity($country, $city) {
        $db = new SQLite3('../newdb.sqlite');

        $ret = $db->query("select Country_Key FROM Country WHERE Name = '" . $country . "'");
        $country_key = $ret->fetchArray();

        $sql = "INSERT INTO Capital_City(Country_Key, Name) VALUES('" . $country_key["Country_Key"] . "', '" . $city . "')";

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
    addnewcity($_POST["country_name"], $_POST["new_city_name"]);

?>