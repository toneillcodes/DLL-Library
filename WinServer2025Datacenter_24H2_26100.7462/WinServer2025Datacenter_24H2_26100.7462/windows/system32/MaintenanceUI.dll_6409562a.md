# Binary Specification: MaintenanceUI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MaintenanceUI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6409562a6b1e9149df8dee56fe6f04e8c686a024e3e5218ec24c71a2d968af57`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2DC0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2ED0` | 7,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2ED0` | 7,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `StartMaintenance` | `0x4CF0` | 200 | UnwindData |  |
| 6 | `StopMaintenance` | `0x4DC0` | 200 | UnwindData |  |
