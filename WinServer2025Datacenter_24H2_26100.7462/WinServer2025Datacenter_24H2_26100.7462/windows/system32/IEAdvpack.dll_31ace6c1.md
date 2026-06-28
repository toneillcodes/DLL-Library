# Binary Specification: IEAdvpack.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\IEAdvpack.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `31ace6c14fe4d8b9b3f7e34d0c41b489c13e4fb03a1a8c57bbf8812642c97461`
* **Total Exported Functions:** 84

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `AdvInstallFile` | `0x2470` | 264 | UnwindData |  |
| 17 | `AdvInstallFileA` | `0x2470` | 264 | UnwindData |  |
| 18 | `AdvInstallFileW` | `0x2580` | 890 | UnwindData |  |
| 55 | `RegInstall` | `0x3DD0` | 149 | UnwindData |  |
| 56 | `RegInstallA` | `0x3DD0` | 149 | UnwindData |  |
| 57 | `RegInstallW` | `0x3E70` | 262 | UnwindData |  |
| 1 | `DelNodeRunDLL32` | `0x5B10` | 117 | UnwindData |  |
| 2 | `DelNodeRunDLL32A` | `0x5B10` | 117 | UnwindData |  |
| 3 | `DoInfInstall` | `0x6370` | 243 | UnwindData |  |
| 4 | `DoInfInstallA` | `0x6370` | 243 | UnwindData |  |
| 5 | `DoInfInstallW` | `0x6470` | 215 | UnwindData |  |
| 8 | `LaunchINFSectionA` | `0x91D0` | 117 | UnwindData |  |
| 12 | `RegisterOCXW` | `0xA1C0` | 441 | UnwindData |  |
| 11 | `RegisterOCX` | `0xA380` | 155 | UnwindData |  |
| 20 | `DelNode` | `0xBE30` | 82 | UnwindData |  |
| 21 | `DelNodeA` | `0xBE30` | 82 | UnwindData |  |
| 22 | `DelNodeRunDLL32W` | `0xBE90` | 104 | UnwindData |  |
| 23 | `DelNodeW` | `0xBF00` | 701 | UnwindData |  |
| 37 | `GetVersionFromFile` | `0xC290` | 124 | UnwindData |  |
| 38 | `GetVersionFromFileA` | `0xC290` | 124 | UnwindData |  |
| 39 | `GetVersionFromFileEx` | `0xC320` | 114 | UnwindData |  |
| 40 | `GetVersionFromFileExA` | `0xC320` | 114 | UnwindData |  |
| 41 | `GetVersionFromFileExW` | `0xC3A0` | 212 | UnwindData |  |
| 42 | `GetVersionFromFileW` | `0xC480` | 523 | UnwindData |  |
| 44 | `LaunchINFSection` | `0xC6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `LaunchINFSectionW` | `0xC6B0` | 929 | UnwindData |  |
| 47 | `NeedReboot` | `0xCA60` | 43 | UnwindData |  |
| 48 | `NeedRebootInit` | `0xCAA0` | 35 | UnwindData |  |
| 67 | `RunSetupCommand` | `0xCAD0` | 275 | UnwindData |  |
| 68 | `RunSetupCommandA` | `0xCAD0` | 275 | UnwindData |  |
| 69 | `RunSetupCommandW` | `0xCBF0` | 474 | UnwindData |  |
| 73 | `TranslateInfString` | `0xCDD0` | 381 | UnwindData |  |
| 74 | `TranslateInfStringA` | `0xCDD0` | 381 | UnwindData |  |
| 78 | `TranslateInfStringW` | `0xCF60` | 351 | UnwindData |  |
| 9 | `LaunchINFSectionEx` | `0xE360` | 117 | UnwindData |  |
| 10 | `LaunchINFSectionExA` | `0xE360` | 117 | UnwindData |  |
| 19 | `CloseINFEngine` | `0x10940` | 38 | UnwindData |  |
| 24 | `ExecuteCab` | `0x10970` | 347 | UnwindData |  |
| 25 | `ExecuteCabA` | `0x10970` | 347 | UnwindData |  |
| 26 | `ExecuteCabW` | `0x10AE0` | 2,063 | UnwindData |  |
| 33 | `FileSaveRestoreOnINF` | `0x11300` | 303 | UnwindData |  |
| 34 | `FileSaveRestoreOnINFA` | `0x11300` | 303 | UnwindData |  |
| 35 | `FileSaveRestoreOnINFW` | `0x11440` | 760 | UnwindData |  |
| 43 | `IsNTAdmin` | `0x11740` | 432 | UnwindData |  |
| 45 | `LaunchINFSectionExW` | `0x11900` | 427 | UnwindData |  |
| 49 | `OpenINFEngine` | `0x11AC0` | 177 | UnwindData |  |
| 50 | `OpenINFEngineA` | `0x11AC0` | 177 | UnwindData |  |
| 51 | `OpenINFEngineW` | `0x11B80` | 252 | UnwindData |  |
| 52 | `RebootCheckOnInstall` | `0x11C90` | 173 | UnwindData |  |
| 53 | `RebootCheckOnInstallA` | `0x11C90` | 173 | UnwindData |  |
| 54 | `RebootCheckOnInstallW` | `0x11D50` | 322 | UnwindData |  |
| 63 | `RegSaveRestoreOnINF` | `0x11EA0` | 250 | UnwindData |  |
| 64 | `RegSaveRestoreOnINFA` | `0x11EA0` | 250 | UnwindData |  |
| 65 | `RegSaveRestoreOnINFW` | `0x11FA0` | 508 | UnwindData |  |
| 70 | `SetPerUserSecValues` | `0x121B0` | 122 | UnwindData |  |
| 71 | `SetPerUserSecValuesA` | `0x121B0` | 122 | UnwindData |  |
| 72 | `SetPerUserSecValuesW` | `0x12230` | 1,679 | UnwindData |  |
| 75 | `TranslateInfStringEx` | `0x128D0` | 392 | UnwindData |  |
| 76 | `TranslateInfStringExA` | `0x128D0` | 392 | UnwindData |  |
| 77 | `TranslateInfStringExW` | `0x12A60` | 95 | UnwindData |  |
| 79 | `UserInstStubWrapper` | `0x12AD0` | 117 | UnwindData |  |
| 80 | `UserInstStubWrapperA` | `0x12AD0` | 117 | UnwindData |  |
| 81 | `UserInstStubWrapperW` | `0x12B50` | 891 | UnwindData |  |
| 82 | `UserUnInstStubWrapper` | `0x12EE0` | 117 | UnwindData |  |
| 83 | `UserUnInstStubWrapperA` | `0x12EE0` | 117 | UnwindData |  |
| 84 | `UserUnInstStubWrapperW` | `0x12F60` | 948 | UnwindData |  |
| 27 | `ExtractFiles` | `0x13500` | 764 | UnwindData |  |
| 28 | `ExtractFilesA` | `0x13500` | 764 | UnwindData |  |
| 29 | `ExtractFilesW` | `0x13810` | 231 | UnwindData |  |
| 58 | `RegRestoreAll` | `0x15CC0` | 105 | UnwindData |  |
| 59 | `RegRestoreAllA` | `0x15CC0` | 105 | UnwindData |  |
| 60 | `RegRestoreAllW` | `0x15D30` | 123 | UnwindData |  |
| 61 | `RegSaveRestore` | `0x15DC0` | 266 | UnwindData |  |
| 62 | `RegSaveRestoreA` | `0x15DC0` | 266 | UnwindData |  |
| 66 | `RegSaveRestoreW` | `0x15ED0` | 1,091 | UnwindData |  |
| 6 | `FileSaveRestore` | `0x17550` | 224 | UnwindData |  |
| 7 | `FileSaveRestoreA` | `0x17550` | 224 | UnwindData |  |
| 13 | `AddDelBackupEntry` | `0x18E00` | 207 | UnwindData |  |
| 14 | `AddDelBackupEntryA` | `0x18E00` | 207 | UnwindData |  |
| 15 | `AddDelBackupEntryW` | `0x18EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `FileSaveMarkNotExist` | `0x18EF0` | 196 | UnwindData |  |
| 31 | `FileSaveMarkNotExistA` | `0x18EF0` | 196 | UnwindData |  |
| 32 | `FileSaveMarkNotExistW` | `0x18FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `FileSaveRestoreW` | `0x18FE0` | 312 | UnwindData |  |
