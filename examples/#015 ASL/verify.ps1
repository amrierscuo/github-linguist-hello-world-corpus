param(
    [Parameter(Mandatory = $true)][string]$AcpicaDirectory,
    [Parameter(Mandatory = $true)][string]$BuildDirectory
)
$ErrorActionPreference = 'Stop'
$toolRoot = [IO.Path]::GetFullPath($AcpicaDirectory)
$buildRoot = [IO.Path]::GetFullPath($BuildDirectory)
$iasl = Join-Path $toolRoot 'iasl.exe'
$acpiexec = Join-Path $toolRoot 'acpiexec.exe'
if (!(Test-Path -LiteralPath $iasl) -or !(Test-Path -LiteralPath $acpiexec)) {
    throw 'Richiesti iasl.exe e acpiexec.exe dalla toolchain ACPICA.'
}
if (Test-Path -LiteralPath $buildRoot) {
    throw 'Usare una cartella di build nuova: la verifica non sovrascrive cartelle esistenti.'
}
New-Item -ItemType Directory -Path $buildRoot | Out-Null
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'hello.asl') -Destination $buildRoot
Push-Location -LiteralPath $buildRoot
try {
    $compiled = & $iasl 'hello.asl' 2>&1
    $compileExit = $LASTEXITCODE
    $compiled | ForEach-Object { Write-Output $_ }
    if ($compileExit -ne 0) { throw 'Compilazione ASL fallita.' }
    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = $acpiexec
    $startInfo.Arguments = '-b "execute HWLD" hello.aml'
    $startInfo.WorkingDirectory = $buildRoot
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $startInfo
    $null = $process.Start()
    $stdout = $process.StandardOutput.ReadToEndAsync()
    $stderr = $process.StandardError.ReadToEndAsync()
    if (!$process.WaitForExit(30000)) {
        $process.Kill()
        throw 'Timeout durante esecuzione ACPICA.'
    }
    $executeExit = $process.ExitCode
    $response = $stdout.Result + $stderr.Result
    Write-Output $response
    $process.Dispose()
    if ($executeExit -ne 0 -or $response -notmatch 'ACPI Debug:\s+"Hello World"' -or
        $response -notmatch '\[String\] Length 0B = "Hello World"') {
        throw 'Il metodo HWLD non ha prodotto il risultato previsto.'
    }
    Write-Output 'PASS: ASL compiled and HWLD printed and returned Hello World'
} finally {
    Pop-Location
}
