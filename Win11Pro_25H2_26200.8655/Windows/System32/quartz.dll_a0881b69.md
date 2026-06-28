# Binary Specification: quartz.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\quartz.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a0881b69b91951dadc3dac2d37beee8c0d365c64d872fb84eebae91d6e52ae3a`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllGetClassObject` | `0x163A0` | 94 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x26660` | 168,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0x4F870` | 505 | UnwindData |  |
| 8 | `DllUnregisterServer` | `0x4FA70` | 34 | UnwindData |  |
| 3 | `AmpFactorToDB` | `0x4FBC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DBToAmpFactor` | `0x4FC20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AMGetErrorTextA` | `0x4FC60` | 218 | UnwindData |  |
| 2 | `AMGetErrorTextW` | `0x4FD40` | 218 | UnwindData |  |
