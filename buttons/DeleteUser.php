<?php
    function deleteuser($firstname, $lastname) {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "DELETE FROM Users WHERE Users.First_Name = '" . $firstname. "' AND Users.Last_Name = '" . $lastname . "'";

        echo "<table>";
                echo "<caption>Users</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>User Key</th><th>First Name</th><th>Last Name</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

        $db->query($sql);

        $ret = $db->query("select * from Users");

        $row = $ret->fetchArray();
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
    deleteuser($_POST["deletefirstname"], $_POST["deletelastname"]);

?>