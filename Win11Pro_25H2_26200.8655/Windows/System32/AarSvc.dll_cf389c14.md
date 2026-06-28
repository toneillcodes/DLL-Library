# Binary Specification: AarSvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AarSvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cf389c146cb3db0df3d53e7ea68ccfdf032a105c38842a3610fead1c014b939b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x99F0` | 72 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x9A40` | 466 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x9C20` | 232 | UnwindData |  |
| 4 | `ServiceMain` | `0x9D10` | 221,487 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
