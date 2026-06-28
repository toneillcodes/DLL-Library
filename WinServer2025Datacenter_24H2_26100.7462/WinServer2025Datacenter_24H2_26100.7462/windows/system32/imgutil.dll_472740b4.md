# Binary Specification: imgutil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\imgutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `472740b49951657348869b6dde78ef70576f96e7249d08c7cd63e02e6b86068f`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DecodeImageEx` | `0x1010` | 2,045 | UnwindData |  |
| 11 | `SniffStream` | `0x1820` | 1,177 | UnwindData |  |
| 10 | `IdentifyMIMEType` | `0x2B00` | 273 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x3B50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllGetClassObject` | `0x3BE0` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DecodeImage` | `0x4070` | 7,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetMaxMIMEIDBytes` | `0x5E50` | 224 | UnwindData |  |
| 1 | `ComputeInvCMAP` | `0x5F70` | 202 | UnwindData |  |
| 2 | `CreateDDrawSurfaceOnDIB` | `0x6040` | 204 | UnwindData |  |
| 3 | `CreateMIMEMap` | `0x6120` | 59 | UnwindData |  |
| 6 | `DitherTo8` | `0x87F0` | 675 | UnwindData |  |
