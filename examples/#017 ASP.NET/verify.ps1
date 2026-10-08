param([Parameter(Mandatory = $true)][string]$BuildDirectory)
$ErrorActionPreference = 'Stop'
$buildRoot = [IO.Path]::GetFullPath($BuildDirectory)
$frameworkRoot = Join-Path $env:WINDIR 'Microsoft.NET\Framework64\v4.0.30319'
$compiler = Join-Path $frameworkRoot 'csc.exe'
$aspnetCompiler = Join-Path $frameworkRoot 'aspnet_compiler.exe'
if (!(Test-Path -LiteralPath $compiler) -or !(Test-Path -LiteralPath $aspnetCompiler)) {
    throw 'Richiesto .NET Framework 4.x per Windows; ASP.NET Core non compila Web Forms.'
}
if (Test-Path -LiteralPath $buildRoot) {
    throw 'Usare una cartella di build nuova: la verifica non sovrascrive cartelle esistenti.'
}
$siteRoot = Join-Path $buildRoot 'site'
$binRoot = Join-Path $siteRoot 'bin'
New-Item -ItemType Directory -Path $binRoot -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'hello.aspx') -Destination $siteRoot
$hostExecutable = Join-Path $binRoot 'VerifyHost.exe'
& $compiler /nologo /target:exe /r:System.Web.dll ('/out:' + $hostExecutable) (Join-Path $PSScriptRoot 'VerifyHost.cs')
if ($LASTEXITCODE -ne 0) { throw 'Compilazione del supporto di verifica fallita.' }
& $aspnetCompiler -v / -p $siteRoot (Join-Path $buildRoot 'precompiled')
if ($LASTEXITCODE -ne 0) { throw 'Compilazione ASP.NET fallita.' }
& $hostExecutable ($siteRoot + [IO.Path]::DirectorySeparatorChar)
if ($LASTEXITCODE -ne 0) { throw 'Esecuzione ASP.NET fallita.' }
