# Binary Specification: LocationFramework.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\LocationFramework.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `967f5fd405840ef1d81295a16eca769869d6cd95c670d0ebb6a2e86563fddd32`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `SvcOnConsoleSessionNotification` | `0x2F460` | 17 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x3A8A0` | 42 | UnwindData |  |
| 1 | `LocationObjectManagerInstance` | `0x41E30` | 108 | UnwindData |  |
| 7 | `SvcLocationReleaseRef` | `0x4BC60` | 32 | UnwindData |  |
| 5 | `SvcLocationAddRef` | `0x4BCE0` | 32 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x58190` | 42 | UnwindData |  |
| 9 | `SvcOnUserLogOnStateNotification` | `0x69F60` | 17 | UnwindData |  |
| 6 | `SvcLocationInitServerLock` | `0x96570` | 112,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllRegisterServer` | `0xB1DC0` | 76 | UnwindData |  |
| 14 | `DllUnregisterServer` | `0xB1E20` | 81 | UnwindData |  |
| 2 | `LocationServiceHostShutdown` | `0xC6700` | 17 | UnwindData |  |
| 3 | `LocationServiceHostStartup` | `0xC6720` | 17 | UnwindData |  |
| 4 | `RegisterLocationCOMServer` | `0xC6740` | 312 | UnwindData |  |
| 10 | `UnregisterLocationCOMServer` | `0xC68C0` | 299 | UnwindData |  |
