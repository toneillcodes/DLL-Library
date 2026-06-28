# Binary Specification: WakeWordEngine.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\detectionverificationdrv.inf_amd64_34be0abce9b5f0cb\WakeWordEngine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `973ec9a3622b92aaa75a4e7b185bcc75d16006dc51a2305d3c0e0b1dd6935aa3`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateWweInstance` | `0x13F0` | 1,519 | UnwindData |  |
| 2 | `GetChunkSizeIn10Ms` | `0x19E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetVendorId` | `0x19F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `OnReferenceSignalLevelChanged` | `0x1A00` | 48 | UnwindData |  |
| 5 | `ReleaseWweInstance` | `0x1A30` | 48 | UnwindData |  |
| 6 | `Reset` | `0x1A60` | 59 | UnwindData |  |
| 7 | `UpdateConfiguration` | `0x1AA0` | 58 | UnwindData |  |
| 8 | `Verify` | `0x1AE0` | 170 | UnwindData |  |
