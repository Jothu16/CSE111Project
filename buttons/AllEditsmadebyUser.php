<?php
    function ALL_Edits_Made_by_User_LowTOHigh() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Users.First_Name, Users.Last_Name, COUNT(UserEdits.User_Key) as cnt " .
                "FROM Users " .
                "INNER JOIN UserEdits ON UserEdits.User_Key = Users.User_Key " .
                "GROUP BY Users.First_Name, Users.Last_Name " .
                "ORDER BY cnt";

                echo "<table>";
                echo "<caption>Amount of edits made by Users</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>First Name</th><th>Last Name</th><th>Edit Count</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

                $ret = $db->query($sql);
                while ($row = $ret->fetchArray()) {
                    echo "<tr>";
                    echo "<td>" . $row["First_Name"] . "</td>" .
                        "<td>" . $row["Last_Name"] . "</td>" .
                        "<td>" . $row["cnt"] . "</td>";
                    echo "</tr>";
                }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    ALL_Edits_Made_by_User_LowTOHigh();

?>