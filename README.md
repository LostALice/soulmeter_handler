<!-- Code by AkinoAlice@Tyrant_Rex -->

# Soulmeter_Handler

![專案封面圖](1.ico)

## Function

- [x] Automatic Update DPS
- [x] Automatic Start up SoulWorker

## Installation

1. Put this application in your DPS directory

1. Create a shortcut and set as "Run as administer"

## Config file
```
{
    "KeepHistoryVision": false,
    "KeepArchive": false,
    "StartSoulWorker": true,
    "RepoOwner": "neonr-0"
}
```
## Config description
- KeepHistoryVision - keep the old vision
- KeepArchive - keep all .zip file
- StartSoulWorker - start both DPS and soulworker
- RepoOwner - set the repo owner

## Built command

```
pyinstaller -F -w --icon=1.ico .\soulmeter_handler.py
```

## Contact
- [x] Discord [Don't you feel your weakness#7031]
