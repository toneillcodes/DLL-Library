# Binary Specification: eapprovp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\eapprovp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b14658f5970bb4c7304960602e1bfda24de62e8efb33fcceed8d6c3043da2ad7`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EapProvPlugGetInfo` | `0x2660` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EapProvPluginDeinitialize` | `0x26C0` | 274 | UnwindData |  |
| 3 | `EapProvPluginInitialize` | `0x2AB0` | 402 | UnwindData |  |
| 4 | `EapProvPluginTestForAuthenticatingWlanInterfaces` | `0x2C50` | 426 | UnwindData |  |
| 5 | `EapProvPluginWlanCloseHandle` | `0x2E00` | 164 | UnwindData |  |
| 6 | `EapProvPluginWlanOpenHandle` | `0x2EB0` | 202 | UnwindData |  |
| 7 | `EapProvPluginWlanRegisterNotification` | `0x2F80` | 242 | UnwindData |  |
