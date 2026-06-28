# Binary Specification: spp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\spp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `739abbba7b13cff5bc3ed3f7e787d2b2af2c75bc4cb8b689eaee6d621fb7fd16`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `SxTracerDebuggerBreak` | `0xCA70` | 80,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x20510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x20530` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x206B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x206C0` | 127 | UnwindData |  |
| 5 | `SppFreeBadWritersArray` | `0x20750` | 94 | UnwindData |  |
| 6 | `SppFreeClientPropArray` | `0x207C0` | 94 | UnwindData |  |
| 7 | `SppFreeExternalGroupPropArray` | `0x20830` | 97 | UnwindData |  |
| 8 | `SppFreeGroupPropArray` | `0x208A0` | 97 | UnwindData |  |
| 9 | `SppFreeMetadataProp` | `0x20910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SxTracerGetThreadContextDebug` | `0x20920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SxTracerGetThreadContextRetail` | `0x20940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SxTracerShouldTrackFailure` | `0x20950` | 65,468 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
