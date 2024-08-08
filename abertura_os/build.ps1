$exclude = @("venv", "abertura_os.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "abertura_os.zip" -Force