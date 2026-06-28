# Binary Specification: LocationFramework.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\LocationFramework.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8ed170b311ad7e0ecb97853ade5173e14a207896463d64349e267bc91acc8555`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `SvcOnConsoleSessionNotification` | `0x319F0` | 17 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x39320` | 42 | UnwindData |  |
| 1 | `LocationObjectManagerInstance` | `0x41E30` | 108 | UnwindData |  |
| 7 | `SvcLocationReleaseRef` | `0x4D960` | 32 | UnwindData |  |
| 5 | `SvcLocationAddRef` | `0x4D9E0` | 32 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x5C980` | 42 | UnwindData |  |
| 9 | `SvcOnUserLogOnStateNotification` | `0x6DA60` | 17 | UnwindData |  |
| 6 | `SvcLocationInitServerLock` | `0x97240` | 122,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllRegisterServer` | `0xB50F0` | 76 | UnwindData |  |
| 14 | `DllUnregisterServer` | `0xB5150` | 81 | UnwindData |  |
| 2 | `LocationServiceHostShutdown` | `0xC9830` | 17 | UnwindData |  |
| 3 | `LocationServiceHostStartup` | `0xC9850` | 17 | UnwindData |  |
| 4 | `RegisterLocationCOMServer` | `0xC9870` | 312 | UnwindData |  |
| 10 | `UnregisterLocationCOMServer` | `0xC99F0` | 299 | UnwindData |  |
