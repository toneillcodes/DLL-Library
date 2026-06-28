# Binary Specification: DmiProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\DmiProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `517233f4c8df0fac32b6ca0386cacb75ef4e2e649d1df53ee0dfa6e67f30c2e4`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3D60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3D90` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3DC0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3F30` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4030` | 114 | UnwindData |  |
