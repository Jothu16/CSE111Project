<?php
    function deletecitydata($city) {
        $db = new SQLite3('../newdb.sqlite');

        $ret = $db->query("select Capital_City.City_Key FROM Capital_City WHERE Capital_City.Name = '" . $city . "'");
        $city_key = $ret->fetchArray();

        $sql = "DELETE FROM Current_AQ_Info WHERE Current_AQ_Info.City_Key = '" . $city_key["City_Key"] . "'";

        echo "<table>";
        echo "<caption>Current Air Quality Information</caption>";
        echo "<thead>";
        echo "<tr>";
        echo "<th>AQ Key</th><th>Date</th><th>AQI Value</th><th>City Key</th>";
        echo "</tr>";
        echo "</thead>";
        echo "<tbody>";

        $db->query($sql);

        $ret = $db->query("select * from Current_AQ_Info");
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
    deletecitydata($_POST["city_name"]);

?>