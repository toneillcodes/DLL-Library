# Binary Specification: UnattendProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\UnattendProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f644828b3a8c307cf615371d777b94cf69d46518196c7c7c93093aefad6b0fd6`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x38A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x38D0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3900` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3A70` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3B70` | 114 | UnwindData |  |
