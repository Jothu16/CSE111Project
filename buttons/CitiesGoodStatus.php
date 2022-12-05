<?php
    function CitiesGoodStatus($status) {
        $db = new SQLite3('../newdb.sqlite');

        $ret = $db->query("select Threshold_Lower, Threshold_Upper FROM Status WHERE Description = '" . $status . "'");
        $threshold = $ret->fetchArray();

        $sql = "SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status " .
        "INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key " .
        "WHERE Current_AQ_Info.AQI_Value >= " . $threshold['Threshold_Lower'] . " " .
        "AND Current_AQ_Info.AQI_Value <= " . $threshold['Threshold_Upper'];

        echo "<table>";
                echo "<caption>Cities with " . $status . " Status</caption>";
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
    CitiesGoodStatus($_POST["status"]);

?>