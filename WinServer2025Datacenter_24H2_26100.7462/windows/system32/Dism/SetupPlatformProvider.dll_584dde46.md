# Binary Specification: SetupPlatformProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\SetupPlatformProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `584dde46ecf026fffee9447d18134a22a3932f4de6e2bbfb9aea37e89a36fb95`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3B10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3B40` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3B70` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3CE0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3DE0` | 114 | UnwindData |  |
