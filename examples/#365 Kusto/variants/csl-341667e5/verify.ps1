param([Parameter(Mandatory=$true)][string]$ParserAssembly)
$ErrorActionPreference = 'Stop'
Add-Type -Path $ParserAssembly
$query = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'hello.csl') -Raw
$code = [Kusto.Language.KustoCode]::ParseAndAnalyze($query)
$diagnostics = @($code.GetDiagnostics())
if ($diagnostics.Count -gt 0) { throw ($diagnostics | Out-String) }
Write-Output ('Kusto parser accepted query; diagnostics: ' + $diagnostics.Count)
