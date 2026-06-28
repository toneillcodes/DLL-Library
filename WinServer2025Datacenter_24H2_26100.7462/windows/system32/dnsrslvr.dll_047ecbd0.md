# Binary Specification: dnsrslvr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dnsrslvr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `047ecbd0b0fb0373137e89eddf1997bef86405f76606752109c5cf3f9915b9bb`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `Reg_DoRegisterAdapter` | `0xFA10` | 506 | UnwindData |  |
| 1 | `LoadGPExtension` | `0x3C850` | 4,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ServiceMain` | `0x3D970` | 115 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x3DA90` | 191,468 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
