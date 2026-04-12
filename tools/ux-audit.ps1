param(
  [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
  [string]$OutputRoot = "",
  [int]$MaxAttempts = 3
)

$ErrorActionPreference = "Stop"

function Get-ChromePath {
  $candidates = @(
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
  )

  foreach ($candidate in $candidates) {
    if (Test-Path -LiteralPath $candidate) {
      return $candidate
    }
  }

  throw "No supported Chromium browser executable was found."
}

function Convert-ToFileUrl {
  param([Parameter(Mandatory = $true)][string]$PathValue)
  return [System.Uri]::new((Resolve-Path $PathValue).Path).AbsoluteUri
}

function Invoke-HeadlessScreenshot {
  param(
    [Parameter(Mandatory = $true)][string]$BrowserPath,
    [Parameter(Mandatory = $true)][string]$Url,
    [Parameter(Mandatory = $true)][string]$Viewport,
    [Parameter(Mandatory = $true)][string]$OutFile,
    [Parameter(Mandatory = $true)][string]$ProfileDir
  )

  $arguments = @(
    "--headless=new",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-background-networking",
    "--disable-background-timer-throttling",
    "--disable-renderer-backgrounding",
    "--disable-features=Translate,OptimizationHints,MediaRouter",
    "--hide-scrollbars",
    "--no-first-run",
    "--no-default-browser-check",
    "--allow-file-access-from-files",
    "--user-data-dir=$ProfileDir",
    "--window-size=$Viewport",
    "--screenshot=$OutFile",
    $Url
  )

  & $BrowserPath @arguments *> $null
  if ($LASTEXITCODE -ne 0) {
    throw "Browser exited with code $LASTEXITCODE while capturing $Url"
  }

  if (-not (Test-Path -LiteralPath $OutFile -PathType Leaf)) {
    throw "Expected screenshot was not created: $OutFile"
  }
}

if (-not $OutputRoot) {
  $OutputRoot = Join-Path $Root ".codex-audit\runs"
}

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$runDir = Join-Path $OutputRoot $timestamp
New-Item -ItemType Directory -Force -Path $runDir | Out-Null

$browserPath = Get-ChromePath
$targets = @(
  @{ Name = "home"; Url = Convert-ToFileUrl (Join-Path $Root "index.html"); Viewport = "1440,2200" },
  @{ Name = "article"; Url = Convert-ToFileUrl (Join-Path $Root "en\math\arithmetic.html"); Viewport = "1440,2600" }
)

$results = @()

foreach ($target in $targets) {
  $outFile = Join-Path $runDir "$($target.Name).png"
  $success = $false

  for ($attempt = 1; $attempt -le $MaxAttempts -and -not $success; $attempt++) {
    $profileDir = Join-Path $runDir ("profile-{0}-{1}" -f $target.Name, $attempt)
    New-Item -ItemType Directory -Force -Path $profileDir | Out-Null

    try {
      Invoke-HeadlessScreenshot `
        -BrowserPath $browserPath `
        -Url $target.Url `
        -Viewport $target.Viewport `
        -OutFile $outFile `
        -ProfileDir $profileDir

      $results += [pscustomobject]@{
        name = $target.Name
        ok = $true
        attempt = $attempt
        file = $outFile
      }
      $success = $true
    }
    catch {
      $results += [pscustomobject]@{
        name = $target.Name
        ok = $false
        attempt = $attempt
        error = $_.Exception.Message
      }

      if ($attempt -lt $MaxAttempts) {
        Start-Sleep -Seconds ([Math]::Min(20, 5 * $attempt))
      }
    }
    finally {
      Remove-Item -LiteralPath $profileDir -Recurse -Force -ErrorAction SilentlyContinue
    }
  }

  if (-not $success) {
    throw "Failed to capture $($target.Name) after $MaxAttempts attempt(s)."
  }
}

$summary = [ordered]@{
  timestamp = (Get-Date).ToString("o")
  root = $Root
  browser = $browserPath
  results = $results
  screenshots = (Get-ChildItem $runDir -Filter *.png | Select-Object Name, Length, LastWriteTime)
  gitStatus = (git -C $Root status --short | Out-String).Trim()
}

$summary | ConvertTo-Json -Depth 6 | Set-Content -Path (Join-Path $runDir "summary.json") -Encoding utf8
Write-Output $runDir
