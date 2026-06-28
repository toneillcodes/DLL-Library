# Binary Specification: RecoveryProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\RecoveryProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a513a9d3a17a01b3316bc3e2923bf1fd34df4958896331b97e114d7ace1d7a8f`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3AF0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3B20` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3C90` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3D90` | 114 | UnwindData |  |
