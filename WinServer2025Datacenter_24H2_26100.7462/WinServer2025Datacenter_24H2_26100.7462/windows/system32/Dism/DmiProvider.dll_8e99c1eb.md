# Binary Specification: DmiProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\DmiProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8e99c1eb37df27579c1e3d40337b45b44131d06d2eaad17221ada369be597890`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3D30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3D60` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3D90` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3F00` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4000` | 114 | UnwindData |  |
