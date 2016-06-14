<?php include_once($APP_ROOT . '/config/db_connect.php'); ?>
<html>
<head> 
	<style>
		td {font-size: 12px; font-weight: bold;}
</style>
</head>
<?php include_once('process_header.php'); ?>
<table>
<?php
if( isset($_POST['person']) ){

$date = date('Y-m-d');
        $date = date('Y-m-d', strtotime(str_replace('-', '/', $date)));
        $mod = $_POST['person'];
        $sid = $_POST['sid'];
        $rating = $_POST['rating'];


        $sql = "UPDATE Image SET img_person = '$mod', img_last_view = '$date', img_rating = '$rating', img_proc_ind = 1 WHERE img_sid = '$sid'";
        try {
                $CHECKNAME = $dbh->prepare($sql);
                $CHECKNAME->execute();
                $CHECKNAME = null;
        }catch (Exception $e) {
                die("Oh noes! There's an error in the query!");
        }


}
?>
<?php
        $sql = "SELECT a.file_name, a.file_sid, a.file_date_added from Image b, File a" 
               . " where b.img_proc_ind = 0 AND a.file_sid = b.img_sid " 
               . " ORDER BY a.file_date_added DESC LIMIT 0,18";
        try {
                $CHECKNAME = $dbh->prepare($sql);
                $CHECKNAME->execute();
?>

		<table>
<?php

                while($row = $CHECKNAME->fetch()) {  
                        $file =  $row['file_name'];
			$sid = $row['file_sid'];
			$dt = $row['file_date_added'];
?>
                <form action="enter_info.php" method="post">

		<tr>
			<td>
				<a href="../../../../tunnel/uplds/<?php echo  $file; ?>"><img src="../../../../tunnel/uplds/<?php echo $file; ?>" height="25%"  /></a>
			</td>
			<td>
				&nbsp;
			</td>
			<td><?php echo $file; ?></td>
			<td><?php echo $sid; ?></td>
<td>
                                date added: <?php echo $dt; ?><input type="submit" value="Enter Info" />
                        </td>
			<td>
				<input type="hidden" value="<?php echo $sid; ?>" name="target_sid" />
			</td>
<?php
                }
                $CHECKNAME = null;
        }catch (Exception $e) {
                die("Oh noes! There's an error in the query!");
        }       

?>

</table>
