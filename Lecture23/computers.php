<!DOCTYPE html>
<html> 

<head>
    <meta charset="utf-8">
    <title>Computers Database</title>
</head>
    
<body>

<form action="process.php" method="get">
   <label>Maker:</label>
   <select name="maker" id="maker">
      <option value=''>------- Select --------</option>

      <?php
         try {
            $db = new SQLite3('../data.sqlite');
            if (!$db) {
               echo $db->lastErrorMsg();
            }
            else {
               echo "Opened database successfully\n";
            }

            $sql =<<<EOF
               SELECT DISTINCT maker FROM Product ORDER BY maker
EOF;

            $ret = $db->query($sql);
            while ($row = $ret->fetchArray()) {
               echo "<option value='". $row['maker']. "'>". $row['maker']. "</option>";
            }
            echo "Operation done successfully\n";

            $db->close();
         }
         catch (Exception $e) {
            echo "<h2 style='width:100%; background-color:ff0000;color:#ffffff;text-align:center;'>Database error!</h2><br/>" . $e;
         }
      ?>
   </select>

   <label>Product type:</label>
   <select name="product" id="product">
      <option value='All'>All</option>
      <option value='PC'>PC</option>
      <option value='Laptop'>Laptop</option>
      <option value='Printer'>Printer</option>
   </select>

   <input type="submit" name="runQ" value="Find">
</form>

</body>

</html>
