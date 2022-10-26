$crossRows = 9

if ($crossRows % 2 -eq 0) {
    $crossWidth = [math]::Round($crossRows/4)
    if ($crossWidth % 2 -ne 0) {
        $crossWidth += 1
    }
    $c1 = $crossRows / 2 - $crossWidth / 2
    $c2 = $c1 + $crossWidth - 1
}
else {
    $crossWidth = [math]::Round($crossRows/4)
    if ($crossWidth % 2 -eq 0) {
        $crossWidth += 1
    }
    $c1 = [math]::Round($crossRows / 2 - $crossWidth / 2)
    $c2 = $c1 + $crossWidth - 1
}

for ($y = 0; $y -lt $crossRows; $y++) {
    for ($x = 0; $x -lt $crossRows; $x++) {
        if (($c1 -le $x -and $x -le $c2) -or ($c1 -le $y -and $y -le $c2)) {
            Write-Host "x" -NoNewline
        }
        else {
            Write-Host " " -NoNewline
        }
    }
    Write-Host
}
