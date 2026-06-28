# Binary Specification: PimIndexMaintenance.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PimIndexMaintenance.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b73b075cfd171987961cf356272c53484dba856fc1720116d60ea50f8d451c7b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateInprocPimimConnectionHandle` | `0x3470` | 388 | UnwindData |  |
| 2 | `PimIMService_ResetInprocService` | `0x3700` | 120 | UnwindData |  |
| 3 | `ServiceMain` | `0xD780` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SvchostPushServiceGlobals` | `0xD810` | 83,084 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
