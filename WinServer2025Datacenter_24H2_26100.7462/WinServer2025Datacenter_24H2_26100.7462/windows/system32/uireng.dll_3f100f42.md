# Binary Specification: uireng.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\uireng.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3f100f42019d54e53665d519b8a31a8ec024eff0927fa1e405e497c778ff0fa5`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `UirFreeRecordedActionInfo` | `0x168D0` | 160 | UnwindData |  |
| 5 | `UirGetRecordedActionInfo` | `0x16980` | 310 | UnwindData |  |
| 6 | `UirGetScreenComment` | `0x16AC0` | 139 | UnwindData |  |
| 7 | `UirInitializeEngine` | `0x16B60` | 245 | UnwindData |  |
| 8 | `UirIsRecordingActive` | `0x16C60` | 167 | UnwindData |  |
| 9 | `UirOutCreateOutputFile` | `0x16D10` | 208 | UnwindData |  |
| 10 | `UirPauseRecordingSession` | `0x16DF0` | 191 | UnwindData |  |
| 11 | `UirResumeRecordingSession` | `0x16EC0` | 204 | UnwindData |  |
| 12 | `UirStartRecordingSession` | `0x16FA0` | 229 | UnwindData |  |
| 13 | `UirStopRecordingSession` | `0x17090` | 158 | UnwindData |  |
| 14 | `UirUninitializeEngine` | `0x17140` | 139 | UnwindData |  |
| 15 | `UirUpdateRecordingSession` | `0x171E0` | 184 | UnwindData |  |
| 16 | `UirWriteRecordedActionAndCommentListMht` | `0x172A0` | 294 | UnwindData |  |
| 17 | `UirWriteRecordedActionListMht` | `0x173D0` | 294 | UnwindData |  |
| 18 | `UirWriteRecordedActionListXml` | `0x17500` | 150 | UnwindData |  |
| 19 | `UirWriteUserComments` | `0x175A0` | 116 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1BCB0` | 106 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x1BD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x1BD30` | 65 | UnwindData |  |
