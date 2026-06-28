# Binary Specification: ISM.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ISM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e587c1ecc421cd5404834e1cfc0188f19ea3933745742c92ce308defe9430e35`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `NotifyInputSinkTransformChanged` | `0x48CA0` | 638 | UnwindData |  |
| 9 | `NotifyInputSinkRemoved` | `0x4B5F0` | 57 | UnwindData |  |
| 8 | `NotifyInputSinkParented` | `0x4B790` | 414 | UnwindData |  |
| 4 | `SetManipulationInputTarget` | `0x6D2E0` | 43 | UnwindData |  |
| 7 | `CreateSystemInputHost` | `0x83320` | 89,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `RegisterManipulationThread` | `0x98F70` | 32,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `IsSystemInputHostStandalone` | `0xA0C90` | 29 | UnwindData |  |
| 2 | `Register3DCompositor` | `0xA33F0` | 37 | UnwindData |  |
| 6 | `Unregister3DCompositor` | `0xA3420` | 28 | UnwindData |  |
| 5 | `StopAndEndInertia` | `0xA3450` | 1,276,523 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
