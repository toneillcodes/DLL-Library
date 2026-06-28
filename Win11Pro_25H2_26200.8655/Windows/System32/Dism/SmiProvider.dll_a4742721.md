# Binary Specification: SmiProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\SmiProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a4742721a6dc1b657852e8fe8f1ff42ae68d4659537a17069f74f30a0fab627f`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x6BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x6C20` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x6C50` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x6DC0` | 304 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6F00` | 166 | UnwindData |  |
