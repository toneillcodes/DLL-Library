# Binary Specification: JHI64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\JHI64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `846f9274606ce97bcc543d101dfd53807e9b26647cc0e21799d827a90fd7366c`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `JHI_Initialize` | `0xA1B0` | 120 | UnwindData |  |
| 3 | `JHI_Deinit` | `0xA620` | 71 | UnwindData |  |
| 2 | `JHI_CreateSession` | `0xABD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `JHI_SendAndRecv2` | `0xABE0` | 183 | UnwindData |  |
| 10 | `JHI_Install2` | `0xAE60` | 560 | UnwindData |  |
| 14 | `JHI_Uninstall` | `0xB090` | 826 | UnwindData |  |
| 5 | `JHI_GetAppletProperty` | `0xB3D0` | 1,764 | UnwindData |  |
| 7 | `JHI_GetSessionsCount` | `0xBAC0` | 853 | UnwindData |  |
| 1 | `JHI_CloseSession` | `0xC1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `JHI_ForceCloseSession` | `0xC1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `JHI_GetSessionInfo` | `0xC1C0` | 163 | UnwindData |  |
| 11 | `JHI_RegisterEvents` | `0xC9B0` | 934 | UnwindData |  |
| 13 | `JHI_UnRegisterEvents` | `0xCD60` | 560 | UnwindData |  |
| 8 | `JHI_GetVersionInfo` | `0xCF90` | 169 | UnwindData |  |
