<br>
<br>
<button onclick="CitiesGoodStatus()">print all cities with a "good" status</button>

<?php
    function CitiesGoodStatus() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
        INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
        WHERE Current_AQ_Info.AQI_Value >= 0
        AND Current_AQ_Info.AQI_Value <= 50";

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
    CitiesGoodStatus();

?>