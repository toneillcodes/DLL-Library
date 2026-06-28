# Binary Specification: SetupPlatformProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\SetupPlatformProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a24b6b10c10249de0423ee42f09933a3ad2ee7ce16218d8212fd06194994fb82`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3B10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3B40` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3B70` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3CE0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3DE0` | 114 | UnwindData |  |
