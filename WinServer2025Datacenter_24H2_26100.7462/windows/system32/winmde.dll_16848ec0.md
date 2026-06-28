# Binary Specification: winmde.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winmde.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16848ec0f5bcda54a9fa220d17a4071072dc9979cfa318b4cebb5faac08adbff`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x40FD0` | 12,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x40FD0` | 12,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x43FC0` | 50 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x44000` | 83 | UnwindData |  |
| 6 | `MFCreateWMPMDEOpCenter` | `0x44370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFCreateWinMDEOpCenter` | `0x44390` | 31,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFCreateNetVRoot` | `0x4BF80` | 473 | UnwindData |  |
