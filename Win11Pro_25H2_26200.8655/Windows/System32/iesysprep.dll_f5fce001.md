# Binary Specification: iesysprep.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\iesysprep.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f5fce001ff334e721d7395ccb76903394554fef2fa7522a1d2b488ea0b70c25b`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Sysprep_Cleanup_IE` | `0x3470` | 565 | UnwindData |  |
| 2 | `Sysprep_Generalize_IE` | `0x36B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `Sysprep_Offline_Specialize_IE` | `0x36C0` | 498 | UnwindData |  |
| 4 | `Sysprep_Online_Specialize_IE` | `0x38C0` | 304 | UnwindData |  |
| 5 | `Sysprep_Specialize_IE` | `0x3A00` | 328 | UnwindData |  |
