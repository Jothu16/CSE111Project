<br>
<br>
<button onclick="Low_and_High_CountryAQI()">print lowest and highest country's AQI Value</button>

<?php
    function Low_and_High_CountryAQI() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "select * FROM ";

        echo "<table>";
                echo "<caption>Current Air Quality Information</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>AQ_Key</th><th>Date</th><th>AQI_Value</th><th>City_Key</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["AQ_Key"] . "</td>" .
                "<td>" . $row["Date"] . "</td>" .
                "<td>" . $row["AQI_Value"] . "</td>" .
                "<td>" . $row["City_Key"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    Low_and_High_CountryAQI();

?>