# Binary Specification: IBSProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\IBSProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `87f904286ce73442d1347bce7814a0544805eba42b447e17a250c2c45a982d81`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3890` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x38C0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3A30` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3B30` | 114 | UnwindData |  |
