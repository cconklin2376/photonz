<html>


<head>
	<style type="text/css">


body {
	background:#cdcbca; 
}


.wrap {
width: 100%;
overflow:auto;
}

.fleft {
    float:left; 
    width: 60%;
    /*background:blue;*/
    background:#cdcbca;
    height: 500px;
}

.fright {
float: right;
    /*background:pink;*/
    height: 500px;
    width: 40%;

}

.container {
    height: 500px;
    width: 500px;
    background-color: red;
    float: left;
    overflow: hidden;
    margin: 20px;
}

img {
    max-width: 100%;
    height: auto;
}

.icon {
	height: 50px;
    width: 50px;
    background-color: red;
    float: left;
    overflow: hidden;
    
}

td {height: 30px;}

input[type="text"] {
    width: 100%;
}
</style>
	<style type="text/css"><!--
	
	        /* style the auto-complete response */
	        li.ui-menu-item { font-size:12px !important; }
	
	--></style> 	

<?php include_once($APP_ROOT . '/config/db_connect.php'); ?>
<?php


	$id = $_POST['target_sid'];
	$sqls = "SELECT file_name from File where file_sid='$id'";
	
	try {
	        $CHECKNAME = $dbh->prepare($sqls);
                $CHECKNAME->execute();
                while($row = $CHECKNAME->fetch()) {  
        	        $view_file =  $row['file_name'];
                }
                $CHECKNAME = null;
        }catch (Exception $e) {
        	die("Oh noes! There's an error in the query!");
        }	

?>
<a href="../mod/new_subject.php">New subject</a><br />
<table>
	<tr>
		<td>Filename:</td>
		<td><?php echo $view_file; ?></td>
		<td>SID: </td>
		<td><?php echo $_POST['target_sid']; ?></td>
	</tr>
	<tr>
		<td><form action="../mod/getname.php" method="post">
			<input type="hidden" value="<?php echo $_POST['target_sid']; ?>" name="sid" />
			<input type="submit" value="Rename" />
		   </form>
		</td>
	</tr>
</table>



	

<div class="wrap">
    <div class="fleft">
        
    	<div class="container">

                <a href="../../../../tunnel/uplds/<?php echo $view_file; ?>"><img src="../../../../tunnel/uplds/<?php echo $view_file; ?>" height="500" width="500"  alt="test image" /></a>
        </div>
    
        
    </div>
    <form action="target.php" method="post">

    <div class="fright">
    	<table>
    		<col width="150">
  			<col width="200">

    		<tr>
    			<td>Subject:</td>
    			<td>


				<select name="subject">
				<?php
					
        $sqls = "SELECT subject_name, subject_id from Subject ORDER BY subject_name";
        
        try {
                $CHECKNAME = $dbh->prepare($sqls);
                $CHECKNAME->execute();
                while($row = $CHECKNAME->fetch()) {  
                        $thename =  $row['subject_name'];
                        $theid =  $row['subject_id'];
                        echo "<option value=\"" . $theid . "\">" . $thename . "</option>"; 
        }
                $CHECKNAME = null;
        }catch (Exception $e) {
                die("Oh noes! There's an error in the query!");
        }       

?>




	</select>

    		</tr>
    		<tr>
    			<td>Rating:</td>
    			<td><input id="rating" autocomplete="off" name="rating" type="text" /></td>
    		</tr>
    		<tr>
    			<td>&nbsp;&nbsp;</td><td><input type="submit" value="Commit" /></td>
    		</tr>
		<tr>
    			<td>Title:</td>
    			<td><input id="title" name="title" type="text" /></td>
    		</tr>
    		<tr>
			<td>Description (120 chars):</td>
			<td><input id="descr" name="descr" type="text" />
    		<tr>
    			<td colspan="2"></td>
    		</tr>
    	</table>
    	
    </div>
	<input type="hidden" value="<?php echo $id; ?>" name="sid" />
   	</form>
    
</div>
