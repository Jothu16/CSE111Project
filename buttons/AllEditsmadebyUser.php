<br>
<br>
<button onclick="ALL_Edits_Made_by_User_LowTOHigh()">count all edits made by users today form lowest to highest</button>

<?php
    function ALL_Edits_Made_by_User_LowTOHigh() {
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
    ALL_Edits_Made_by_User_LowTOHigh();

?>