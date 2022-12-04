<?php
    function count_history_users() {
            $db = new SQLite3('../newdb.sqlite');

            $sql = "select count(History.History_Key) as total " .
                    "from History " .
                    "UNION " .
                    "select count(Users.User_Key) as total " . 
                    "from Users";
                    
            echo "<table>";
            echo "<caption>Totals</caption>";
            echo "<tbody>";

            $ret = $db->query($sql);
            $row = $ret->fetchArray();
                
            echo "<tr>";
            echo "<td>User Count: " . $row['total'] . "</td>";
            echo "</tr>";

            $row = $ret->fetchArray();
                
            echo "<tr>";
            echo "<td>History Count: " . $row['total'] . "</td>";
            echo "</tr>";

            echo "</tbody>";
            echo "</table>";

            $db->close();
        }

    count_history_users();
?>