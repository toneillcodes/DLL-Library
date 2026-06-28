# Binary Specification: NetworkUXBroker.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\NetworkUXBroker.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `14abbd9c964f032f28df7752adab30d719dc894fca7e267beb3c46bafd07a386`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9770` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x97B0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x97F0` | 134 | UnwindData |  |
| 4 | `DllMain` | `0x9880` | 370 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x9A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x9A30` | 257,452 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
