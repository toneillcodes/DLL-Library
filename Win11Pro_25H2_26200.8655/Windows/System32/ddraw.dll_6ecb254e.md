# Binary Specification: ddraw.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ddraw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6ecb254e345551566e454be2c807e99adae3add23490df3d87e152f3dc0e7707`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DirectDrawCreateEx` | `0x8450` | 254 | UnwindData |  |
| 8 | `DirectDrawCreate` | `0x8740` | 130 | UnwindData |  |
| 12 | `DirectDrawEnumerateExA` | `0x107B0` | 1,289 | UnwindData |  |
| 1 | `AcquireDDThreadLock` | `0x2FDD0` | 136 | UnwindData |  |
| 21 | `ReleaseDDThreadLock` | `0x31890` | 11,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CompleteCreateSysmemSurface` | `0x345F0` | 423 | UnwindData |  |
| 20 | `RegisterSpecialCase` | `0x36950` | 317 | UnwindData |  |
| 5 | `DDInternalLock` | `0x46870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DDInternalUnlock` | `0x46890` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetDDSurfaceLocal` | `0x46940` | 92 | UnwindData |  |
| 3 | `D3DParseUnknownCommand` | `0x46B00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DirectDrawEnumerateA` | `0x46BA0` | 55 | UnwindData |  |
| 13 | `DirectDrawEnumerateExW` | `0x46BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DirectDrawEnumerateW` | `0x46BF0` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DDGetAttachedSurfaceLcl` | `0x473A0` | 180 | UnwindData |  |
| 7 | `DSoundHelp` | `0x48BF0` | 127 | UnwindData |  |
| 9 | `DirectDrawCreateClipper` | `0x4ACF0` | 235 | UnwindData |  |
| 15 | `DllCanUnloadNow` | `0x4B7F0` | 209 | UnwindData |  |
| 16 | `DllGetClassObject` | `0x4B8D0` | 524 | UnwindData |  |
| 18 | `GetOLEThunkData` | `0x4CCA0` | 107 | UnwindData |  |
| 19 | `GetSurfaceFromDC` | `0x4E8B0` | 28,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SetAppCompatData` | `0x55870` | 183,778 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
