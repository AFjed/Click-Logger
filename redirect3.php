<?php
// Log the click
$logMessage = "Someone clicked the link: https://blog.boxmode.com/top-funny-websites/";
// Replace 'your_webhook_url_here' with your actual Discord webhook URL
$webhookUrl = 'https://discord.com/api/webhooks/1218947479999877151/nloZbM1-6HP8SZkD1illqnEl_vvPUOA2FHXH0hPy9YzJJ-Qec0SSO9MYXeBye7InhQW3';
$payload = json_encode(array('content' => $logMessage));

$ch = curl_init($webhookUrl);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

$result = curl_exec($ch);
curl_close($ch);

// Redirect the user to the intended destination
header("Location: https://blog.boxmode.com/top-funny-websites/");
exit;
?>
