# Binary Specification: UiaManager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UiaManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e289d58eb8b5486bd77b48f72e774b7fcdef453e8da5e177fb71717103d4f303`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllGetClassObject` | `0xCAD0` | 689 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0xD590` | 75 | UnwindData |  |
| 5 | `GetProxyDllInfo` | `0x279D0` | 233,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `UiaInitCrossMachineConnection` | `0x60B60` | 362 | UnwindData |  |
| 2 | `UiaInitCrossMachineConnectionW` | `0x60B60` | 362 | UnwindData |  |
