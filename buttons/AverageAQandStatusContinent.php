<br>
<br>
<button onclick="AverageAQ_andAverageStatus_Continent()">print average air quality and the average status of each continent</button>

<?php
    function AverageAQ_andAverageStatus_Continent() {
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
    AverageAQ_andAverageStatus_Continent();

?>