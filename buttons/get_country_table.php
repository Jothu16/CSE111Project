<?php
    function get_country() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM Country";

        echo "<table>";
                echo "<caption>Country</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Country_Key</th><th>Cont_Key</th><th>Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
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
    get_country();

?>