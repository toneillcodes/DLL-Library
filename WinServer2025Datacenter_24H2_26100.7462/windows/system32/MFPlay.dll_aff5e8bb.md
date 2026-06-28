# Binary Specification: MFPlay.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MFPlay.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aff5e8bb491ed86d7b790fdaf78b4f1ce6d8a1113d9f6a4562639e9d10014e34`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x68B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x68D0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x6B40` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x6BB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFPCreateMediaPlayer` | `0x6BF0` | 545 | UnwindData |  |
| 6 | `MFPCreateMediaPlayerEx` | `0x6E20` | 555 | UnwindData |  |
