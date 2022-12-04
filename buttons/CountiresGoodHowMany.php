<br>
<br>
<button onclick="Continents_withCountry_Good_HowMany()">print all continents with a country with "good" status and how many</button>

<?php
    function Continents_withCountry_Good_HowMany() {
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
    Continents_withCountry_Good_HowMany();

?>