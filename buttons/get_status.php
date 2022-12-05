<?php
    function get_history_status() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM Status";

        echo "<table>";
                echo "<caption>Status</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Status_Key</th><th>Description</th><th>Lower Threshold</th><th>Upper Threshold</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Status_Key"] . "</td>" .
                "<td>" . $row["Description"] . "</td>" .
                "<td>" . $row["Threshold_Lower"] . "</td>" .
                "<td>" . $row["Threshold_Upper"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    get_history_status();

?>