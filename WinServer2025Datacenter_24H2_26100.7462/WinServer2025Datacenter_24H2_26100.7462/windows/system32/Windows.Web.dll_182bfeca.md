# Binary Specification: Windows.Web.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Web.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `182bfecaffb1cda5f45b53d5a7bb5683f32438ce05358e9cfbb48710a6bf87b1`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x12E60` | 83 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x133F0` | 58 | UnwindData |  |
| 4 | `DllMain` | `0x15A00` | 81 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x47C20` | 134 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x47CB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x47CE0` | 71,292 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
