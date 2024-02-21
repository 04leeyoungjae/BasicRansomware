<?php
if (isset($_POST['message'])) 
{
	$message=$_POST['message'];
	$file='message.txt';
	file_put_contents($file,$message.PHP_EOL,FILE_APPEND | LOCK_EX);
}
else
{
	echo "No message received!";
}
?>
