# Binary Specification: mssecwfpu.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mssecwfpu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b5b10daf218356a6c0dbd9bbf091d7164aa12ee2bf5bb090c4ff89a44c9aa1ac`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SecSetWfpGuardConfiguration` | `0x4D00` | 432 | UnwindData |  |
| 2 | `SecWfpAllowDriverUnload` | `0x4EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SecWfpClose` | `0x4EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SecWfpOpen` | `0x4ED0` | 100 | UnwindData |  |
