<?php
    function get_history() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM History";

        echo "<table>";
                echo "<caption>History</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>History_Key</th><th>Date</th><th>AQI_Value</th><th>City_Key</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["History_Key"] . "</td>" .
                "<td>" . $row["Date"] . "</td>" .
                "<td>" . $row["AQI_Value"] . "</td>" .
                "<td>" . $row["City_Key"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    get_history();

?>