@echo off

REM Get the current logged on username
set USERNAME=%USERNAME%

REM Define the directory path
set GNUPG_PATH=C:\Users\%USERNAME%\AppData\Roaming\gnupg

REM Ensure the directory exists
if not exist "%GNUPG_PATH%" (
    echo Creating directory: %GNUPG_PATH%
    mkdir "%GNUPG_PATH%"
)

REM Create gpg-agent.conf with the text "enable-putty-support"
echo enable-putty-support > "%GNUPG_PATH%\gpg-agent.conf"
echo Created file: %GNUPG_PATH%\gpg-agent.conf with content: enable-putty-support

REM Create scdaemon.conf with the text "reader-port "Yubico YubiKey OTP+CCID 0""
echo reader-port "Yubico YubiKey OTP+CCID 0" > "%GNUPG_PATH%\scdaemon.conf"
echo Created file: %GNUPG_PATH%\scdaemon.conf with content: reader-port "Yubico YubiKey OTP+CCID 0"

REM Optional: Notify the user that the operation was successful
echo Files created successfully!

REM Optional: Pause the script to see the output before the window closes
pause