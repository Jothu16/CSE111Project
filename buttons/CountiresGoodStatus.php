<?php
    function Countries_Good_Status($status) {
        $db = new SQLite3('../newdb.sqlite');

        $ret = $db->query("select Threshold_Lower, Threshold_Upper FROM Status WHERE Description = '" . $status . "'");
        $threshold = $ret->fetchArray();

        $sql = "SELECT Country.Name as Name FROM Current_AQ_Info, Capital_City, Country " .
        "WHERE Current_AQ_Info.City_Key = Capital_City.City_Key " .
        "AND Capital_City.Country_Key = Country.Country_Key " .
        "AND Capital_City.Name IN (SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status " .
                                      "INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key " .
                                      "WHERE Current_AQ_Info.AQI_Value >= " . $threshold['Threshold_Lower'] . " " .
                                      "AND Current_AQ_Info.AQI_Value <= " . $threshold['Threshold_Upper'] . ")";

        echo "<table>";
                echo "<caption>Countries with " . $status . " Status</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Country Name</th>";
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
    Countries_Good_Status($_GET["status"]);

?>