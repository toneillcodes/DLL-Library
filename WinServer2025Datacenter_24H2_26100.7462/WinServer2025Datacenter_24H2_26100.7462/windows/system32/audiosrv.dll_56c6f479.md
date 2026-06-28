# Binary Specification: audiosrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\audiosrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `56c6f4791ab885efc3691e3a3ee21c6134d12c7bc54ba6ab0f6c5cb170d03a86`
* **Total Exported Functions:** 2

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0x144720` | 755 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x144A70` | 150,555 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
