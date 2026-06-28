# Binary Specification: dnsrslvr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dnsrslvr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4fe072fe4eacd8c97dbafef3e6b1b6a7049971c0a0e6ac863dd33d36cd04a960`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `Reg_DoRegisterAdapter` | `0x21CB0` | 541 | UnwindData |  |
| 1 | `LoadGPExtension` | `0x3CE20` | 4,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ServiceMain` | `0x3DFF0` | 120 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x3E110` | 257,820 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
