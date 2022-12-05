<?php
    function get_user_edits() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM UserEdits";

        echo "<table>";
                echo "<caption>User Edits</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>AQ_Key</th><th>User_Key</th><th>City_Key</th><th>Date</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["AQ_Key"] . "</td>" .
                "<td>" . $row["User_Key"] . "</td>" .
                "<td>" . $row["City_Key"] . "</td>" .
                "<td>" . $row["Date"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    get_user_edits();

?>