<?php
    function get_history_status() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM Users";

        echo "<table>";
                echo "<caption>Users</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>User_Key</th><th>First_Name</th><th>Last_Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["User_Key"] . "</td>" .
                "<td>" . $row["First_Name"] . "</td>" .
                "<td>" . $row["Last_Name"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    get_history_status();

?>