# Binary Specification: ChxEM.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\InputMethod\SHARED\ChxEM.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f441e53e689618b466cf22ff4357f63f3efa96236805008b4bc93b891f8fc5a0`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x4980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x4990` | 210 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4A70` | 52 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4AB0` | 38 | UnwindData |  |
| 1 | `DestroyMtf` | `0x9150` | 112 | UnwindData |  |
| 6 | `SetupMtf` | `0x93D0` | 44 | UnwindData |  |
