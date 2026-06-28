# Binary Specification: FXSOCM.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\setup\FXSOCM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd934dfabaf3e792219c507c58a120eacf4b70dbcca46afd627db4a879b37856`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `SecureFaxServiceDirectories` | `0x1E00` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `FaxModemCoClassInstaller` | `0x21D0` | 449 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x3500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x3520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllRegisterServer` | `0x3550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x3570` | 34,316 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
