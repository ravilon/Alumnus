# Define the host variable
$hostAddress = '192.168.8.82'  # Change this to your desired default host address

# Check if the host variable is empty, and if so, set it to 0.0.0.0
if ([string]::IsNullOrEmpty($hostAddress)) {
    $hostAddress = '0.0.0.0'
}

# Run Flask application
$command = "& flask --app main run --host='$hostAddress' --port=5000 --debug"
Invoke-Expression -Command $command
