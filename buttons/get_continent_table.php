<?php
    function get_continent() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM Continent";

        echo "<table>";
                echo "<caption>Continent</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Cont_Key</th><th></th><th>Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Cont_Key"] . "</td>" .
                "<td>" . $row["Name"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    get_continent();

?>