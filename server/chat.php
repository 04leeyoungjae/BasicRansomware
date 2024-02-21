<?php
function isValidHex($input) {
    return preg_match('/^[0-9a-fA-F]{8}$/', $input);
}

date_default_timezone_set('Asia/Seoul');

$id = htmlspecialchars($_POST['id']);
$message = htmlspecialchars($_POST['message']);

if ($id === 'KEEPER') {
    exit("Invalid hex ID.");
}

if (!empty($id) && !empty($message)) {
    $log = fopen("chat_log.txt", "a");

    // Get user's IP address unless it's KEEPER
    $ip = '';
    if ($id !== 'KEEPER') {
        $ip = $_SERVER['REMOTE_ADDR'];
    }

    // Check if the hashed ID matches the target hash
    $hashedId = hash('sha256',$id);
    $targetHash = '1ee7eab69550fd00549b2d4f79d1c1606e252fe6ac84d8911467d14d4c6edc8f'; // SHA256 hash of KEEPER
    if ($hashedId === $targetHash) {
        $id = 'KEEPER'; // Change the ID to KEEPER
		$ip = '';
	}

    if ($id !== 'KEEPER' && !isValidHex($id)) {
        exit("Invalid hex ID.");
    }

    // Format message with nickname and IP address (unless it's KEEPER)
    $formattedMessage = "[".date("Y-m-d H:i:s") . "] " . $id;
    if ($ip !== '') {
        $formattedMessage .= "(" . $ip . ")";
    }
    $formattedMessage .= " : " . $message . "\n";

    if ($id === "KEEPER") {
        $formattedMessage = "<span style='color: blue; font-weight: bold;'>" . $formattedMessage . "</span>";
    }

    fwrite($log, $formattedMessage);
    fclose($log);
}
?>

