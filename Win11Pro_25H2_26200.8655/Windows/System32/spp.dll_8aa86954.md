# Binary Specification: spp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\spp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8aa86954eb0e3fede63e062a60c34b3df8b05ad5368591b1f2dcab0cadc72575`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `SxTracerDebuggerBreak` | `0xCBF0` | 80,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x20690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x206B0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x20830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x20840` | 127 | UnwindData |  |
| 5 | `SppFreeBadWritersArray` | `0x208D0` | 94 | UnwindData |  |
| 6 | `SppFreeClientPropArray` | `0x20940` | 94 | UnwindData |  |
| 7 | `SppFreeExternalGroupPropArray` | `0x209B0` | 97 | UnwindData |  |
| 8 | `SppFreeGroupPropArray` | `0x20A20` | 97 | UnwindData |  |
| 9 | `SppFreeMetadataProp` | `0x20A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SxTracerGetThreadContextDebug` | `0x20AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SxTracerGetThreadContextRetail` | `0x20AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SxTracerShouldTrackFailure` | `0x20AD0` | 88,140 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
