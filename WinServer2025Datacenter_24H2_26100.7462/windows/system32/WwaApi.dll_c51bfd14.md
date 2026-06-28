# Binary Specification: WwaApi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WwaApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c51bfd146c956c404755a0390d002b2314819278faebcfa7593550e482ee9b6c`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x22F0` | 146 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x5F10` | 110 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xD190` | 121 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xD210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xD240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetProxyDllInfo` | `0xD270` | 253,380 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
