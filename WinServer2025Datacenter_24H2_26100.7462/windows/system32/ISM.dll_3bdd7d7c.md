# Binary Specification: ISM.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ISM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3bdd7d7c69e596de692bdd07039ad86a8a5807cd9c3d90b89d7ab007efde5f8b`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `NotifyInputSinkTransformChanged` | `0x4CBC0` | 638 | UnwindData |  |
| 9 | `NotifyInputSinkRemoved` | `0x4E180` | 57 | UnwindData |  |
| 8 | `NotifyInputSinkParented` | `0x4E320` | 414 | UnwindData |  |
| 4 | `SetManipulationInputTarget` | `0x6CC70` | 43 | UnwindData |  |
| 7 | `CreateSystemInputHost` | `0x83450` | 89,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `RegisterManipulationThread` | `0x990F0` | 31,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `IsSystemInputHostStandalone` | `0xA0D80` | 29 | UnwindData |  |
| 2 | `Register3DCompositor` | `0xA3400` | 37 | UnwindData |  |
| 6 | `Unregister3DCompositor` | `0xA3430` | 28 | UnwindData |  |
| 5 | `StopAndEndInertia` | `0xA3460` | 1,285,083 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
