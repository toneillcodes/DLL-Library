# Binary Specification: wbiosrvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbiosrvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `93fa405fce7ae3341b9c8eada01a67efe995ce22299d34dfbe1bc70d4d6f11de`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `SvchostPushServiceGlobals` | `0x47330` | 26,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ServiceMain` | `0x4DB70` | 735 | UnwindData |  |
| 1 | `OutOfProcessExceptionEventCallback` | `0x5F310` | 173 | UnwindData |  |
| 2 | `OutOfProcessExceptionEventDebuggerLaunchCallback` | `0x5F3D0` | 56 | UnwindData |  |
| 3 | `OutOfProcessExceptionEventSignatureCallback` | `0x5F410` | 657 | UnwindData |  |
