# Binary Specification: PimIndexMaintenance.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\PimIndexMaintenance.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `786562d59eed0af097e1761df750fb8362aafbdae1033293e0541e8e752f8a9a`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateInprocPimimConnectionHandle` | `0x3470` | 388 | UnwindData |  |
| 2 | `PimIMService_ResetInprocService` | `0x3700` | 120 | UnwindData |  |
| 3 | `ServiceMain` | `0xD780` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SvchostPushServiceGlobals` | `0xD810` | 83,132 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
