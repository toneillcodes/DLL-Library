# Binary Specification: colorui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\colorui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `04ebba4b4354181b82dd0c3de561bfc1c3d8ba3ecc4120a2c3775869726e26fe`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `LaunchColorCpl` | `0x6630` | 794 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xBCE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xBD20` | 362 | UnwindData |  |
| 4 | `DllMain` | `0xBE90` | 340 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xBFF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0xC030` | 57,356 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
