# Binary Specification: WwaApi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WwaApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cc7e600226b793721799a959c0e707ba10d8f6dab767b18042b14949b783b829`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x2300` | 146 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x5F20` | 110 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xD1D0` | 121 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xD250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xD280` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetProxyDllInfo` | `0xD2B0` | 252,372 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
