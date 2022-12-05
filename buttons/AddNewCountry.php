<?php
    function addnewcountry($new_country, $continent) {
        $db = new SQLite3('../newdb.sqlite');

        $ret = $db->query("select Cont_Key FROM Continent WHERE Name = '" . $continent . "'");
        $cont_key = $ret->fetchArray();

        $sql = "INSERT INTO Country(Cont_Key, Name) VALUES('" . $cont_key["Cont_Key"] . "', '" . $new_country . "')";

        echo "<table>";
                echo "<caption>Country</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Country Key</th><th>Continent Key</th><th>Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

        $db->query($sql);

        $ret = $db->query("select * from Country");
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Country_Key"] . "</td>" .
                "<td>" . $row["Cont_Key"] . "</td>" .
                "<td>" . $row["Name"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    addnewcountry($_POST["new_country_name"], $_POST["continent_name"]);

?>