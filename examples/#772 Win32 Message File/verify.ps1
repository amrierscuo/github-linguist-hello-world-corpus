param([Parameter(Mandatory=$true)][string]$LibraryPath)
$ErrorActionPreference='Stop'
Add-Type -TypeDefinition @'
using System;
using System.Text;
using System.Runtime.InteropServices;
public static class CorpusMessages {
 [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
 public static extern IntPtr LoadLibraryExW(string name, IntPtr file, uint flags);
 [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
 public static extern uint FormatMessageW(uint flags, IntPtr source, uint id, uint language, StringBuilder buffer, uint size, IntPtr arguments);
 [DllImport("kernel32.dll")] public static extern bool FreeLibrary(IntPtr handle);
}
'@
$handle=[CorpusMessages]::LoadLibraryExW($LibraryPath,[IntPtr]::Zero,2)
if($handle -eq [IntPtr]::Zero){throw "LoadLibraryExW failed"}
try {
 $buffer=New-Object System.Text.StringBuilder 256
 $length=[CorpusMessages]::FormatMessageW(0xA00,$handle,1,0x409,$buffer,256,[IntPtr]::Zero)
 if($length -eq 0){throw "FormatMessageW failed"}
 $message=$buffer.ToString().TrimEnd([char[]]"`r`n")
 if($message -ne 'Hello, World!'){throw "Unexpected resource message"}
 Write-Output $message
 Write-Output 'PASS: Windows FormatMessageW loads the original compiled English message resource'
} finally {[void][CorpusMessages]::FreeLibrary($handle)}
