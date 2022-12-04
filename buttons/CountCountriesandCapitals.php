<?php
    function count_amount_countries_and_capitals() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select COUNT(Capital_City.City_Key) as city_total, COUNT(Country.Country_Key) as country_total " .
                "FROM Capital_City, Country " .
                "where Capital_City.Country_Key = Country.Country_Key";

        echo "<table>";
        echo "<caption>Totals</caption>";
        echo "<tbody>";

        $ret = $db->query($sql);
        $row = $ret->fetchArray();
            
        echo "<tr>";
        echo "<td>Country Total: " . $row['country_total'] . "</td>";
        echo "</tr>";
            
        echo "<tr>";
        echo "<td>City Total: " . $row['city_total'] . "</td>";
        echo "</tr>";

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    count_amount_countries_and_capitals();

?>