# Cria o atalho "Fafa" na area de trabalho apontando para Fafa.bat, com o icone do Fafa.
# Uso: powershell -ExecutionPolicy Bypass -File backend\scripts\criar_atalho.ps1

$raiz    = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$alvo    = Join-Path $raiz "Fafa.bat"
$icone   = Join-Path $raiz "src\fafa.ico"
$desktop = [Environment]::GetFolderPath("Desktop")
$atalho  = Join-Path $desktop "Fafa.lnk"

if (-not (Test-Path $alvo)) { throw "Fafa.bat nao encontrado em $raiz" }

$shell = New-Object -ComObject WScript.Shell
$lnk = $shell.CreateShortcut($atalho)
$lnk.TargetPath       = $alvo
$lnk.WorkingDirectory = $raiz
$lnk.Description      = "Fafa - assistente da SIZE Engenharia"
if (Test-Path $icone) { $lnk.IconLocation = "$icone,0" }
$lnk.Save()

Write-Output "Atalho criado: $atalho"
