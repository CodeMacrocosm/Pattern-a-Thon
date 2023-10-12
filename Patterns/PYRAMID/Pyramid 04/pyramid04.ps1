$pyramidRows = 5
for ($i = 1; $i -le $pyramidRows * 2; $i+=2) {
    Write-Host "$(" "*([math]::Floor($pyramidRows - $i / 2)))" -NoNewline
    for ($j = 1; $j -le $i; $j++) {
        Write-Host "$($j)" -NoNewline
    }
    Write-Host
}
