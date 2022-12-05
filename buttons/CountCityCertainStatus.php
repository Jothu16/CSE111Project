<br>
<br>
<button onclick="Amount_City_Specific_Status()">count the amount of times each city had a certain status</button>

<?php
    function Amount_City_Specific_Status() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Capital_City.Name, Status.Description, COUNT(Status.Description)
        FROM History, HistoryStatus, Status
        INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
        WHERE History.History_Key = HistoryStatus.History_Key
        AND Status.Status_Key = HistoryStatus.Status_Key
        GROUP BY Capital_City.Name, Status.Description
        ORDER BY Capital_City.Name, Status.Threshold_Lower";

        echo "<table>";
                echo "<caption>Current Air Quality Information</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>AQ_Key</th><th>Date</th><th>AQI_Value</th><th>City_Key</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["AQ_Key"] . "</td>" .
                "<td>" . $row["Date"] . "</td>" .
                "<td>" . $row["AQI_Value"] . "</td>" .
                "<td>" . $row["City_Key"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    Amount_City_Specific_Status();

?>