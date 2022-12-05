<?php
    function get_city() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM Capital_City";

        echo "<table>";
                echo "<caption>Capital City</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>City_Key</th><th>Country_Key</th><th>Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
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
    get_city();

?>