<?php
    function ALL_Cities_Change_in_Status_and_Orderdate() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT History.Date, Capital_City.Name, Status.Description " .
        "FROM History, HistoryStatus, Status, Capital_City, (SELECT Capital_City.Name as cities " .
                                 "FROM History, Status, HistoryStatus " .
                                 "INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key " .
                                 "WHERE History.History_Key = HistoryStatus.History_Key " .
                                 "AND Status.Status_Key = HistoryStatus.Status_Key " .
                                 "GROUP BY Capital_City.Name " .
                                 "HAVING COUNT(DISTINCT Status.Description) > 1 " .
                                 "ORDER BY Capital_City.Name, Status.Threshold_Lower) AS cities_with_change " .
        "WHERE History.History_Key = HistoryStatus.History_Key " .
        "AND HistoryStatus.Status_Key = Status.Status_Key " .
        "AND History.City_Key = Capital_City.City_Key " .
        "AND Capital_City.Name = cities_with_change.cities";

        echo "<table>";
                echo "<caption>History of Change in Air Quality</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Date</th><th>Name</th><th>Status</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Date"] . "</td>" .
                "<td>" . $row["Name"] . "</td>" .
                "<td>" . $row["Description"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    ALL_Cities_Change_in_Status_and_Orderdate();

?>