<?php
    function GetCurrentUserKey($firstname, $lastname) {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select Users.User_Key FROM Users WHERE Users.First_Name = '" . $firstname . 
        "' and Users.Last_Name = '" . $lastname . "'";

        echo "<table>";
        echo "<tbody>";


        $ret = $db->query($sql);
        $user_key = $ret->fetchArray();

        echo "<tr>";
        echo "<td>User Key: " . $user_key['User_Key'] . "</td>";
        echo "</tr>";

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    GetCurrentUserKey($_POST["Firstname"], $_POST["Lastname"]);

?>