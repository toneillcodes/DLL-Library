# Binary Specification: DetectionVerificationDrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\intcoed.inf_amd64_dd6a7ef14d856351\AS\IAS\DetectionVerificationDrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eb8bb9d8d8736ce9a2d35e4df743eecfdd33d8ea97477056b3e617f13e0516b6`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Cleanup` | `0x2B20` | 33 | UnwindData |  |
| 3 | `Initialize` | `0x2B50` | 87 | UnwindData |  |
| 4 | `Reset` | `0x2BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SetArmed` | `0x2BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `UpdateDvConfiguration` | `0x2BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `UpdateMicGeoConfiguration` | `0x2C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `UpdatePPConfiguration` | `0x2C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `UpdateReferenceWovConfiguration` | `0x2C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `UpdateWovConfiguration` | `0x2C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Verify` | `0x2C80` | 105 | UnwindData |  |
| 2 | `FxDriverEntryUm` | `0x9700` | 324,156 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
