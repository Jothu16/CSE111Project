<?php
    function ALL_Cities_Except_Unhealthy($status) {
        $db = new SQLite3('../newdb.sqlite');

        $ret = $db->query("select Threshold_Lower FROM Status WHERE Description = '" . $status . "'");
        $threshold = $ret->fetchArray();

        $sql = "SELECT Capital_City.Name FROM Current_AQ_Info
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                  EXCEPT
                  SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    WHERE Current_AQ_Info.AQI_Value >= " . $threshold["Threshold_Lower"];

                    echo "<table>";
                    echo "<caption>Cities Better than " . $status . "</caption>";
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
    ALL_Cities_Except_Unhealthy($_GET["status"]);

?>