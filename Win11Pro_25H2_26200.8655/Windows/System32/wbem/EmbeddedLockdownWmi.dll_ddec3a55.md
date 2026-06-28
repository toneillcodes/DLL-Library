# Binary Specification: EmbeddedLockdownWmi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\EmbeddedLockdownWmi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ddec3a5550be3e2668ce29bd3003f8e102ebb78c24702a92aaedb2f59ca3720c`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x2900` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2990` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x29D0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x2A50` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2AB0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2B00` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2D20` | 46,860 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
