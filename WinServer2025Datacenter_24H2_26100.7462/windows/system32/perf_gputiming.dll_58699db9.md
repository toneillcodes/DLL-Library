# Binary Specification: perf_gputiming.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\perf_gputiming.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `58699db9032ccb401d6ffaca9b29be18341b22a8d29f9e35ebc7747a27570a08`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CreateETWViewerSynchronizer` | `0x3FA0` | 258 | UnwindData |  |
| 6 | `DisplayFeatureSupport` | `0x5C30` | 221 | UnwindData |  |
| 14 | `GetFeatureSupport` | `0x5FC0` | 862 | UnwindData |  |
| 1 | `CleanUpViewerSyncObjects` | `0x6580` | 60 | UnwindData |  |
| 2 | `CreateCallbackSync` | `0x6750` | 108 | UnwindData |  |
| 4 | `CreateViewerSync` | `0x6A60` | 139 | UnwindData |  |
| 7 | `GetInfosourceVersion` | `0x7470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetMarkerNameTable` | `0x7480` | 276 | UnwindData |  |
| 12 | `DllRegisterServer` | `0x7D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllUnregisterServer` | `0x7D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `UpdateZoomInfo` | `0x7D80` | 97 | UnwindData |  |
| 10 | `DllCanUnloadNow` | `0xDA00` | 42 | UnwindData |  |
| 11 | `DllGetClassObject` | `0xDA30` | 302 | UnwindData |  |
| 5 | `DesktopDuplicationProvider` | `0x32D60` | 2,147 | UnwindData |  |
