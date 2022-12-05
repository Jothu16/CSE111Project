<?php
    function updatefile($old_date, $new_date) {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "UPDATE Current_AQ_Info SET Date = '" . $new_date . "' WHERE Date = '" . $old_date . "'";

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

        $db->close();
    }
    updatefile($_POST["old_date"], $_POST["new_date"]);

?>