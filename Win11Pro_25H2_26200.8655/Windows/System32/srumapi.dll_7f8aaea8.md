# Binary Specification: srumapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\srumapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7f8aaea84a8e2e4f0a57075a9576645e6f26aa698cf7e255988e98817bcce718`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `SruFreeRecordSet` | `0x12B0` | 26 | UnwindData |  |
| 12 | `SruRegisterRealTimeStats` | `0x14B0` | 28 | UnwindData |  |
| 15 | `SruUpdateStats` | `0x19C0` | 482 | UnwindData |  |
| 11 | `SruQueryStatsEx` | `0x1BB0` | 854 | UnwindData |  |
| 9 | `SruQueryStats` | `0x1F10` | 854 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2EE0` | 70 | UnwindData |  |
| 14 | `SruUnregisterRealTimeStats` | `0x2F30` | 183 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x32C0` | 5,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x46D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x4710` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SruCreateCheckpoint` | `0x48C0` | 223 | UnwindData |  |
| 6 | `SruCreateEnergyNotificationServer` | `0x49B0` | 211 | UnwindData |  |
| 7 | `SruDeleteStatsByAppName` | `0x4A90` | 223 | UnwindData |  |
| 10 | `SruQueryStatsBySeqNumber` | `0x4B80` | 272 | UnwindData |  |
| 13 | `SruRetrieveEnergyRecord` | `0x4CA0` | 267 | UnwindData |  |
