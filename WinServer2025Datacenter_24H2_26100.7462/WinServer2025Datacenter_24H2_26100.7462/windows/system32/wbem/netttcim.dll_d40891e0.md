# Binary Specification: netttcim.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\netttcim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d40891e078d308ae334ec25a0dedee5e28dd79e88a10759dd4eddf13ca51b655`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1010` | 54 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1A40` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x1AC0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1B20` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1B70` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1C90` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x1DE0` | 101,184 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
