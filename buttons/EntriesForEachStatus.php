<?php
    function EntriesForEachStatus() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Status.Description, COUNT(Status.Description) as cnt " .
        "FROM Current_AQ_Info, Status " .
        "INNER JOIN Capital_City ON Capital_City.City_Key = Current_AQ_Info.City_Key " .
        "WHERE Current_AQ_Info.AQI_Value >= Status.Threshold_Lower " .
        "AND Current_AQ_Info.AQI_Value <= Status.Threshold_Upper " .
        "GROUP BY Status.Description " .
        "ORDER BY COUNT(Status.Description) DESC";

        echo "<table>";
                echo "<caption>Status Count</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Status</th><th>Count</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Description"] . "</td>" .
                "<td>" . $row["cnt"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    EntriesForEachStatus();

?>