# Binary Specification: FXST30.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\FXST30.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `873e5280c181206e2dea86ba2d51122de65705d802080fb7c1b4f8a29ad96611`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FaxDevAbortOperation` | `0x1D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FaxDevEndJob` | `0x1DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FaxDevInitialize` | `0x1DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FaxDevReceive` | `0x1DC0` | 132 | UnwindData |  |
| 6 | `FaxDevReportStatus` | `0x1E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FaxDevSend` | `0x1E60` | 161 | UnwindData |  |
| 8 | `FaxDevShutdown` | `0x1F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `FaxDevStartJob` | `0x1F20` | 29,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x92F0` | 322 | UnwindData |  |
| 10 | `FaxExtInitializeConfig` | `0x10380` | 173,516 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
