# Binary Specification: Chakradiag.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Chakradiag.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `409769291bfd77f580c293697b5426e995e2e3aeb2e751c51f8eb27d7218e4bd`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0xA570` | 41 | UnwindData |  |
| 4 | `DllGetClassObject` | `0xA5A0` | 319 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xA6F0` | 227 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0xA7E0` | 49,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetDumpStreams` | `0x16910` | 115 | UnwindData |  |
| 1 | `FreeDumpStreams` | `0x16990` | 74 | UnwindData |  |
