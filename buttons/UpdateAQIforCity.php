<?php
    function updateAQIforcity($user_key, $city, $date, $aqi_val) {
        $db = new SQLite3('../newdb.sqlite');

        //login
        $ret = $db->query("select User_Key FROM Users WHERE User_Key = '" . $user_key . "'");
        $check = $ret->fetchArray();

        if (!is_int($check["User_Key"])){
            echo "Invalid User";
            return;
        }

        //Update Current_AQ_Info
        else {
            $ret = $db->query("select Capital_City.City_Key FROM Capital_City WHERE Capital_City.Name = '" . $city . "'");
            $city_key = $ret->fetchArray();

            $sql = "update Current_AQ_Info SET Date = '" . $date .
                "', AQI_Value = " . $aqi_val .
                " WHERE City_Key = " . $city_key['City_Key'] . "";

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

            //Update UserEdits

            $ret = $db->query("select AQ_Key FROM Current_AQ_Info WHERE City_Key = " . $city_key["City_Key"]);
            $aq_key = $ret->fetchArray();

            echo "<table>";
            echo "<caption>User Edits</caption>";
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

            $sql = "INSERT INTO History(Date, AQI_Value, City_Key) VALUES('" . $date . "', " . $aqi_val . ", " . $city_key["City_Key"] . ")";

            echo "<table>";
            echo "<caption>History</caption>";
            echo "<thead>";
            echo "<tr>";
            echo "<th>AQ Key</th><th>User Key</th><th>City Key</th><th>Date</th>";
            echo "</tr>";
            echo "</thead>";
            echo "<tbody>";

            $db->query($sql);

            $ret = $db->query("select * from History");
            while ($row = $ret->fetchArray()) {
                echo "<tr>";
                echo "<td>" . $row["History_Key"] . "</td>" .
                    "<td>" . $row["Date"] . "</td>" .
                    "<td>" . $row["AQI_Value"] . "</td>" .
                    "<td>" . $row["City_Key"] . "</td>";
                echo "</tr>";
            }

            //update historystatus

            $ret = $db->query("select History_Key FROM History WHERE City_Key = " . $city_key["City_Key"] . " AND Date = '" . $date . "'");
            $history_key = $ret->fetchArray();

            $sql = "INSERT INTO HistoryStatus(History_Key, Status_Key, City_Key) " .
                "VALUES(" . $history_key['History_Key'] . ", " . ceil($aqi_val / 50) . ", " . $city_key["City_Key"] . ")";

            echo "<table>";
            echo "<caption>History Status</caption>";
            echo "<thead>";
            echo "<tr>";
            echo "<th>History Key</th><th>Status Key</th><th>City Key</th>";
            echo "</tr>";
            echo "</thead>";
            echo "<tbody>";

            $db->query($sql);

            $ret = $db->query("select * from HistoryStatus");
            while ($row = $ret->fetchArray()) {
                echo "<tr>";
                echo "<td>" . $row["History_Key"] . "</td>" .
                    "<td>" . $row["Status_Key"] . "</td>" .
                    "<td>" . $row["City_Key"] . "</td>";
                echo "</tr>";
            }

            $db->close();
            }
    }
    updateAQIforcity($_POST["login"], $_POST["city_name"], $_POST["new_date"], $_POST["new_AQI_value"]);

?>