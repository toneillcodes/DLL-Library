# Binary Specification: NPSM.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\NPSM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `94154852f195da985ff6634640314d513f984714c21f899bd07a3f720ee71792`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x4C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetActivationFactory` | `0x4C70` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4CB0` | 65 | UnwindData |  |
| 4 | `ServiceMain` | `0x71A0` | 423 | UnwindData |  |
| 5 | `SvchostPushServiceGlobals` | `0x7350` | 105,495 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
