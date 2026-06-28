# Binary Specification: cscobj.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cscobj.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `51f3bfb759c5e7bc67ea8ffca910a96e0f3e4fdcf2c3038174f3bc629ab9dc9c`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllGetClassObject` | `0x59B0` | 40 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x60F0` | 57 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x105E0` | 63 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0x10630` | 63 | UnwindData |  |
| 1 | `ProcessGroupPolicy` | `0x12830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ProcessPolicy` | `0x12850` | 26 | UnwindData |  |
