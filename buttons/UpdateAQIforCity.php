<?php
    include('GetCurrentUserkey.php');

    function updateAQIforcity($user_key, $city, $date, $aqi_val) {
        $db = new SQLite3('../newdb.sqlite');

        //Update Current_AQ_Info

        $ret = $db->query("select Capital_City.City_Key FROM Capital_City WHERE Capital_City.Name = '" . $city . "'");
        $city_key = $ret->fetchArray();

        $sql = "update Current_AQ_Info SET Date = '" . $date . 
        "', AQI_Value = " . $aqi_val .
        " WHERE City_Key = " . $city_key['City_Key'] . "";

        echo "<table>";
                echo "<caption>" . $city_key['City_Key'] . "</caption>";
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

        //Update UserEdits

        $ret = $db->query("select AQ_Key FROM Current_AQ_Info WHERE City_Key = " . $city_key["City_Key"]);
        $aq_key = $ret->fetchArray();

        echo "<table>";
                echo "<caption> User Edits</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>AQ Key</th><th>User Key</th><th>City Key</th><th>Date</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

        $sql = "INSERT INTO UserEdits(AQ_Key, User_Key, City_Key, Date) VALUES(" . $aq_key["AQ_Key"] . ", " . $user_key . 
        ", " . $city_key["City_Key"] . ", '" . $date . "')";
        
        $db->query($sql);

        $ret = $db->query("select * from UserEdits");
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["AQ_Key"] . "</td>" .
                "<td>" . $row["User_Key"] . "</td>" .
                "<td>" . $row["City_Key"] . "</td>" .
                "<td>" . $row["Date"] . "</td>";
            echo "</tr>";
        }

        //update history

        $db->close();
    }
    updateAQIforcity($_POST["login"], $_POST["city_name"], $_POST["new_date"], $_POST["new_AQI_value"]);

?>