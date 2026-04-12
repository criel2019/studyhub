param(
  [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
  [int]$RetryCount = 3
)

$ErrorActionPreference = "Continue"

$runnerLog = Join-Path $Root ".codex-audit\runner.log"
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $runnerLog) | Out-Null

function Write-RunnerLog {
  param([Parameter(Mandatory = $true)][string]$Message)
  Add-Content -LiteralPath $runnerLog -Value ("[{0}] {1}" -f (Get-Date).ToString("s"), $Message) -Encoding utf8
}

$completed = $false

for ($attempt = 1; $attempt -le $RetryCount -and -not $completed; $attempt++) {
  try {
    Write-RunnerLog "Audit attempt $attempt started."
    $runDir = & powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot "ux-audit.ps1") -Root $Root
    if ($LASTEXITCODE -ne 0) {
      throw "ux-audit.ps1 exited with code $LASTEXITCODE"
    }

    Write-RunnerLog "Audit attempt $attempt completed. Output: $runDir"
    $completed = $true
  }
  catch {
    Write-RunnerLog "Audit attempt $attempt failed. $($_.Exception.Message)"
    if ($attempt -lt $RetryCount) {
      Start-Sleep -Seconds ([Math]::Min(30, 10 * $attempt))
    }
  }
}

if (-not $completed) {
  Write-RunnerLog "Audit failed after $RetryCount attempts. Loop will continue."
}
