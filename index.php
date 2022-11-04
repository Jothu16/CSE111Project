<?php
   class MyDB extends SQLite3 {
      function __construct() {
         $this->open('mydb.db');
      }
   }
   $db = new MyDB();
   if(!$db) {
      echo $db->lastErrorMsg();
   } else {
      echo "Opened database successfully\n";
   }

   $sql =<<<EOF
      SELECT * from mytable;
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
      echo "Date = ". $row['Date'] . "\n\n";
      echo "Country = ". $row['Country'] ."\n\n";
      echo "Status = ". $row['Status'] ."\n\n";
      echo "AQI_Value = ".$row['AQI_Value'] ."\n\n";
   }
   echo "Operation done successfully\n";
   $db->close();
?>