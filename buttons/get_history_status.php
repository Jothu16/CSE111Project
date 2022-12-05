<?php
    function get_history_status() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM HistoryStatus";

        echo "<table>";
                echo "<caption>HistoryStatus</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>History_Key</th><th>Status_Key</th><th>City_Key</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["History_Key"] . "</td>" .
                "<td>" . $row["Status_Key"] . "</td>" .
                "<td>" . $row["City_Key"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    get_history_status();

?>