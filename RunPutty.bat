@echo off

REM Notify the user that the GPG agent is being terminated
echo Terminating the GPG agent...
gpgconf --kill gpg-agent

REM Check if the previous command was successful
if %errorlevel%==0 (
    echo GPG agent terminated successfully.
) else (
    echo Failed to terminate the GPG agent.
)

REM Notify the user that the GPG agent is being reloaded
echo Reloading the GPG agent...
gpg-connect-agent reloadagent /bye

REM Check if the reload command was successful
if %errorlevel%==0 (
    echo GPG agent reloaded successfully.
) else (
    echo Failed to reload the GPG agent.
)

REM Optional: Pause the script to see the output before the window closes
pause