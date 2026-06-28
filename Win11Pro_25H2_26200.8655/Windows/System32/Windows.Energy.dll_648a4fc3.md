# Binary Specification: Windows.Energy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Energy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `648a4fc37de9eee80963407a2fc3d9a5f2e7aa0d2b5ec642bcef6d2d259f5596`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE760` | 38 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xE790` | 165 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xE840` | 111 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xE980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xE9B0` | 168,195 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
