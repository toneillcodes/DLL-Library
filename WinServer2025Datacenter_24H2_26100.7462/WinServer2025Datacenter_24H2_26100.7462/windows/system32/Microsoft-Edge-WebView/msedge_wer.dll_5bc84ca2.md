# Binary Specification: msedge_wer.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\msedge_wer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5bc84ca22d8153159f89d38a8dcd67eb52b373e6a90d73e20e61a414c77f4f4b`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `OutOfProcessExceptionEventCallback` | `0x1010` | 107 | UnwindData |  |
| 2 | `OutOfProcessExceptionEventDebuggerLaunchCallback` | `0x1080` | 53,886 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `OutOfProcessExceptionEventSignatureCallback` | `0x1080` | 53,886 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
