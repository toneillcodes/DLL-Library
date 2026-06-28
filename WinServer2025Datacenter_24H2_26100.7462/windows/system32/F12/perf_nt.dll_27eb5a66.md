# Binary Specification: perf_nt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\F12\perf_nt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `27eb5a66c2a9e1627642941d6cd456cfdf54d03120f86bfeea0f760af478019b`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x68B20` | 10,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x68B20` | 10,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x6B3B0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x6B3E0` | 282,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `QueryModernApplicationData` | `0xB0510` | 428,793 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
