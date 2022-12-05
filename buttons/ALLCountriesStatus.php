<br>
<br>
<button onclick="ALL_Countries_Status()">select all countries status</button>

<?php
    function ALL_Countries_Status() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Country.Name, Status.Description FROM Current_AQ_Info, Status, Capital_City, Country
        WHERE Current_AQ_Info.AQI_Value >= Status.Threshold_Lower
        AND Current_AQ_Info.AQI_Value <= Status.Threshold_Upper
        AND Current_AQ_Info.City_Key = Capital_City.City_Key
        AND Capital_City.Country_Key = Country.Country_Key";

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
    ALL_Countries_Status();

?>