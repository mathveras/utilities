# Windows (Not Yet Tested)

$extensionsFile = "extensions.txt"

if (-not (Test-Path $extensionsFile)) {
    Write-Host "❌ Error: '$extensionsFile' not found!"
    exit 1
}

Write-Host "⚙️ Starting VS Code extensions installation..."

Get-Content $extensionsFile | ForEach-Object {
    # Skips comments and empty lines
    if ($_ -match "^\s*#" -or [string]::IsNullOrWhiteSpace($_)) { return }

    # Extracts extension IDs
    $extId = ($_ -replace "#.*", "").Trim()

    Write-Host "🔧 Installing: $extId" -ForegroundColor Yellow

    # Filters unwanted VS Code CLI messages
    $output = code --install-extension $extId 2>&1 | ForEach-Object {
        if ($_ -notmatch "Installing extensions?") {
            $_
        }
    }

    # Shows remaining outputs, if any
    if ($output) { $output }

    # Checks exit code
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed: $extId" -ForegroundColor Red
    }
}

Write-Host "✅ Done! Check above for any errors."
