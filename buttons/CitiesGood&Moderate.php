<br>
<br>
<button onclick="Cities_GoodModerate_Status_History()">find cities that had both "Good" and "Moderate" Statuses in its history - change variables if needed</button>

<?php
    function Cities_GoodModerate_Status_History() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT DISTINCT Capital_City.Name FROM History, HistoryStatus
        INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
        WHERE HistoryStatus.Status_Key = 1
        AND History.History_Key = HistoryStatus.History_Key
      INTERSECT
      SELECT DISTINCT Capital_City.Name FROM History, HistoryStatus
        INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
        WHERE HistoryStatus.Status_Key = 2
        AND History.History_Key = HistoryStatus.History_Key";

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
    Cities_GoodModerate_Status_History();

?>