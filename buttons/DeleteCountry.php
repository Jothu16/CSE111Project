<?php
    function deletecountry($country) {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "DELETE FROM Country WHERE Country.Name = '" . $country. "'";

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
    deletecountry($_POST["country_name"]);

?>