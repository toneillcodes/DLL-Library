# Binary Specification: msiwer.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msiwer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eaa2a0525acb2ab615ea1536f659e8bdcaa49e724c0d049c71fff7391e7f64b2`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `OutOfProcessExceptionEventCallback` | `0x1BD0` | 338 | UnwindData |  |
| 2 | `OutOfProcessExceptionEventDebuggerLaunchCallback` | `0x1D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `OutOfProcessExceptionEventSignatureCallback` | `0x1D50` | 706 | UnwindData |  |
