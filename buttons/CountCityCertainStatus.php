<?php
    function Amount_City_Specific_Status() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Capital_City.Name, Status.Description, COUNT(Status.Description) as cnt " .
        "FROM History, HistoryStatus, Status " .
        "INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key " .
        "WHERE History.History_Key = HistoryStatus.History_Key " .
        "AND Status.Status_Key = HistoryStatus.Status_Key " .
        "GROUP BY Capital_City.Name, Status.Description " .
        "ORDER BY Capital_City.Name, Status.Threshold_Lower";

        echo "<table>";
                echo "<caption>City Status Count</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Name</th><th>Status</th><th>Count</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Name"] . "</td>" .
                "<td>" . $row["Description"] . "</td>" .
                "<td>" . $row["cnt"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    Amount_City_Specific_Status();

?>