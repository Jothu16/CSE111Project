<br>
<br>
<button onclick="myFunction()">find cities that had both "Good" and "Moderate" Statuses in its history - change variables if needed</button>

<?php
    function count_countries_and_capitals() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "";

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
count_countries_and_capitals();

?>