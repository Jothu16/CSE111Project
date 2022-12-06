<?php
    function Cities_GoodModerate_Status_History($status1, $status2) {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT DISTINCT Capital_City.Name FROM History, HistoryStatus, Status " .
        "INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key " .
        "WHERE History.History_Key = HistoryStatus.History_Key " .
        "AND HistoryStatus.Status_Key = Status.Status_Key " .
        "AND Description = '" . $status1 . "' " .
        "INTERSECT " .
        "SELECT DISTINCT Capital_City.Name FROM History, HistoryStatus, Status " .
        "INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key " .
        "WHERE History.History_Key = HistoryStatus.History_Key " .
        "AND HistoryStatus.Status_Key = Status.Status_Key " .
        "AND Description = '" . $status2 . "'";

        echo "<table>";
                echo "<caption>Cities with " . $status1 . " and " . $status2 . " Status</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>City Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Name"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    Cities_GoodModerate_Status_History($_GET["status1"], $_GET["status2"]);

?>