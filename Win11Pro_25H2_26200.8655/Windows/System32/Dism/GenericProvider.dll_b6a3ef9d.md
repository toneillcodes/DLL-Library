# Binary Specification: GenericProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\GenericProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b6a3ef9d7855c1493aad721917a8e63d99160468d09e20f4580cd696e4e3858e`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3CB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3CE0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3D10` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3E80` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3F80` | 114 | UnwindData |  |
