$pyramidRows = 5
for ($i = 1; $i -le $pyramidRows * 2; $i+=2) {
    Write-Output "$(" "*([math]::Floor($pyramidRows - $i / 2)))$("*" * $i)"
}
