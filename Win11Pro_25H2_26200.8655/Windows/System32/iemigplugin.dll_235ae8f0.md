# Binary Specification: iemigplugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\iemigplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `235ae8f02069d3b985aa4d9faafdca37dc93ba88c5b92e8c6e816f45f50bd962`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllInstall` | `0x92D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x92D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x92D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x9300` | 93 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x9370` | 3,610 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
