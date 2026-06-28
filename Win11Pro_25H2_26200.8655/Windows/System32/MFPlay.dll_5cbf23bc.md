# Binary Specification: MFPlay.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MFPlay.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5cbf23bcdeb63c08a8b60fccf584c16fae54b4b602d578986475d9ccf5aeaa59`
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
