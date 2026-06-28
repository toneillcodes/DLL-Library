# Binary Specification: ddraw.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ddraw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `311586666e69904b3eda3b803bd714f69eed172ad4374f518a47c20c14313af9`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DirectDrawCreateEx` | `0x8470` | 254 | UnwindData |  |
| 8 | `DirectDrawCreate` | `0x8760` | 130 | UnwindData |  |
| 12 | `DirectDrawEnumerateExA` | `0x107D0` | 1,289 | UnwindData |  |
| 1 | `AcquireDDThreadLock` | `0x2FDF0` | 136 | UnwindData |  |
| 21 | `ReleaseDDThreadLock` | `0x318B0` | 11,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CompleteCreateSysmemSurface` | `0x34610` | 423 | UnwindData |  |
| 20 | `RegisterSpecialCase` | `0x36970` | 317 | UnwindData |  |
| 5 | `DDInternalLock` | `0x46890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DDInternalUnlock` | `0x468B0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetDDSurfaceLocal` | `0x46960` | 92 | UnwindData |  |
| 3 | `D3DParseUnknownCommand` | `0x46B20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DirectDrawEnumerateA` | `0x46BC0` | 55 | UnwindData |  |
| 13 | `DirectDrawEnumerateExW` | `0x46C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DirectDrawEnumerateW` | `0x46C10` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DDGetAttachedSurfaceLcl` | `0x473C0` | 180 | UnwindData |  |
| 7 | `DSoundHelp` | `0x48C10` | 127 | UnwindData |  |
| 9 | `DirectDrawCreateClipper` | `0x4AD10` | 235 | UnwindData |  |
| 15 | `DllCanUnloadNow` | `0x4B810` | 209 | UnwindData |  |
| 16 | `DllGetClassObject` | `0x4B8F0` | 524 | UnwindData |  |
| 18 | `GetOLEThunkData` | `0x4CCC0` | 107 | UnwindData |  |
| 19 | `GetSurfaceFromDC` | `0x4E8D0` | 28,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SetAppCompatData` | `0x558A0` | 185,090 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
