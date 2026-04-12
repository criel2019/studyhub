Set-Location 'F:\work\studyhub'

powershell -ExecutionPolicy Bypass -File 'C:\Users\User\.codex\skills\loop\scripts\loop.ps1' run-loop `
  -Name 'studyhub-ux' `
  -Command "powershell -ExecutionPolicy Bypass -File .\tools\ux-audit-runner.ps1" `
  -IntervalMinutes 30 `
  -WorkingDirectory 'F:\work\studyhub'
