# Binary Specification: wbiosrvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbiosrvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `202ac12f12c62fe6d631b87efb5d098728d7753f9b29d94fc404727f5c5f3da5`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `SvchostPushServiceGlobals` | `0x41DA0` | 41,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ServiceMain` | `0x4BEC0` | 798 | UnwindData |  |
| 1 | `OutOfProcessExceptionEventCallback` | `0x64B40` | 173 | UnwindData |  |
| 2 | `OutOfProcessExceptionEventDebuggerLaunchCallback` | `0x64C00` | 56 | UnwindData |  |
| 3 | `OutOfProcessExceptionEventSignatureCallback` | `0x64C40` | 657 | UnwindData |  |
