<br>
<br>
<button onclick="ALL_Cities_Except_Unhealthy()">find all cities except for unhealthy or worse cities</button>

<?php
    function ALL_Cities_Except_Unhealthy() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Capital_City.Name FROM Current_AQ_Info
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                  EXCEPT
                  SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    WHERE Current_AQ_Info.AQI_Value >= 101";

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
    ALL_Cities_Except_Unhealthy();

?>