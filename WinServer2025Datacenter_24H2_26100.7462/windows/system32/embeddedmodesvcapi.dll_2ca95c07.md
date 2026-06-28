# Binary Specification: embeddedmodesvcapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\embeddedmodesvcapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2ca95c0705245efe606dc316e95f1c20253e2e526f6655dfc82751642f58e9bb`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ActivatePackage` | `0x6D40` | 261 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x7440` | 81 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x74A0` | 466 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x7680` | 232 | UnwindData |  |
| 5 | `IsEmbeddedModeAllowed` | `0x77A0` | 811 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
