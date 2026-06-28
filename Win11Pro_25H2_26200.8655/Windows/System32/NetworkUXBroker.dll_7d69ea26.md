# Binary Specification: NetworkUXBroker.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\NetworkUXBroker.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7d69ea2623517bb67c9a5c649369bdc250e74faeb9702a2af64b2cf8215ab8a9`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9860` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x98A0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x98E0` | 134 | UnwindData |  |
| 4 | `DllMain` | `0x9970` | 370 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x9AF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x9B20` | 243,036 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
