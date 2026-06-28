# Binary Specification: DetectionVerificationDrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\detectionverificationdrv.inf_amd64_34be0abce9b5f0cb\DetectionVerificationDrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4fd7633c870d75b3921ff6299507315c5351030cfd4d37fa91e74c2cd531dc6d`
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
