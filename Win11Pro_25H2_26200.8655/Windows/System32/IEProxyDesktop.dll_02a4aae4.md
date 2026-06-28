# Binary Specification: IEProxyDesktop.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IEProxyDesktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `02a4aae4395b1d2ed44971cf57bd37cb6303bd85f0f7b26e28ad41af24167016`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllCanUnloadNow` | `0x1D80` | 47 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x1DC0` | 218 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x1ED0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x1F00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetProxyDllInfo` | `0x1F30` | 9,014 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
