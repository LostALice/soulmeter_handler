<!-- Code by AkinoAlice@Tyrant_Rex -->

# Soulmeter_Handler

![icon](1.ico)

## Function

- [x] Automatic Update DPS
- [x] Automatic Start up SoulWorker

## Installation

1. Put this application in your DPS directory

1. Create a shortcut and set as "Run as administer"

## Config file
```
{
    "StartSoulWorker": true,
    "KeepArchive": false,
    "RepoOwner": "neonr-0"
}
```
## Config description
- StartSoulWorker - start both DPS and soulworker
- KeepArchive - keep all .zip file
- RepoOwner - set the repo owner
- KeepFont - keep font file

## Built command

```
pyinstaller -F -w --icon=1.ico --onefile .\soulmeter_handler.py
```

## Contact
- [x] Discord [warabimochiwaikagadesuka]