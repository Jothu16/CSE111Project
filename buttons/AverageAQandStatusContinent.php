<br>
<br>
<button onclick="AverageAQ_andAverageStatus_Continent()">print average air quality and the average status of each continent</button>

<?php
    function AverageAQ_andAverageStatus_Continent() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Continent.Name, Status.Description, AVG(Current_AQ_Info.AQI_Value) 
        FROM Current_AQ_Info, Status
        INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
        INNER JOIN Country ON Capital_City.Country_Key = Country.Country_Key
        INNER JOIN Continent ON Country.Cont_Key = Continent.Cont_Key
        WHERE Current_AQ_Info.AQI_Value >= Status.Threshold_Lower
        AND Current_AQ_Info.AQI_Value <= Status.Threshold_Upper
        GROUP BY Continent.Name";

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
    AverageAQ_andAverageStatus_Continent();

?>