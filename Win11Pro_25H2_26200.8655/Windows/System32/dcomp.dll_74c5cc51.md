# Binary Specification: dcomp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dcomp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `74c5cc517ca9dc5b6a8a727d18e15b6ab75828b3f7a782e3cfdded333de67f54`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1019 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `win32u.NtCreateCompositionInputSink` |
| 1028 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `win32u.NtDesktopCaptureBits` |
| 1043 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `win32u.NtCompositionSetDropTarget` |
| 1044 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `win32u.NtCreateImplicitCompositionInputSink` |
| 1045 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `win32u.NtDCompositionCommitSynchronizationObject` |
| 1046 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `win32u.NtDCompositionGetFrameStatistics` |
| 2503 | *Ordinal Only* | `0x2620` | 158 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x63E60` | 63 | UnwindData |  |
| 2002 | *Ordinal Only* | `0x65B30` | 134 | UnwindData |  |
| 1031 | *Ordinal Only* | `0x905B0` | 304 | UnwindData |  |
| 2501 | *Ordinal Only* | `0x93C70` | 252 | UnwindData |  |
| 2001 | *Ordinal Only* | `0xAC3C0` | 134 | UnwindData |  |
| 1024 | `DllCanUnloadNow` | `0xB4A00` | 42 | UnwindData |  |
| 1025 | `DllGetActivationFactory` | `0xB4A30` | 45 | UnwindData |  |
| 1101 | `DCompositionGetStatistics` | `0xB77B0` | 47 | UnwindData |  |
| 1029 | `DwmFlush` | `0xB77F0` | 3,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `DwmpEnableDDASupport` | `0xB77F0` | 3,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `DCompositionGetTargetStatistics` | `0xB8680` | 37 | UnwindData |  |
| 2502 | *Ordinal Only* | `0xBA5F0` | 2,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `DCompositionCreateSurfaceHandle` | `0xBB110` | 136 | UnwindData |  |
| 1040 | *Ordinal Only* | `0xBE790` | 35 | UnwindData |  |
| 1104 | `DCompositionWaitForCompositorClock` | `0xC0E60` | 25,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | *Ordinal Only* | `0xC7150` | 231 | UnwindData |  |
| 1100 | `DCompositionGetFrameId` | `0xCD0E0` | 27 | UnwindData |  |
| 1103 | `DCompositionBoostCompositorClock` | `0xD9820` | 27 | UnwindData |  |
| 1038 | *Ordinal Only* | `0xDC630` | 4,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `DCompositionCreateDevice3` | `0xDD720` | 12,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | *Ordinal Only* | `0xE06F0` | 108 | UnwindData |  |
| 1021 | `DCompositionCreateDevice2` | `0xE1220` | 13,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | *Ordinal Only* | `0xE47A0` | 199 | UnwindData |  |
| 1020 | `DCompositionCreateDevice` | `0xEA740` | 128,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `DwmEnableMMCSS` | `0x109EA0` | 27 | UnwindData |  |
| 1017 | `DCompositionAttachMouseDragToHwnd` | `0x109ED0` | 110 | UnwindData |  |
| 1018 | `DCompositionAttachMouseWheelToHwnd` | `0x109F50` | 110 | UnwindData |  |
| 2505 | *Ordinal Only* | `0x109FD0` | 27 | UnwindData |  |
| 2007 | *Ordinal Only* | `0x10A000` | 11,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | *Ordinal Only* | `0x10CD80` | 138 | UnwindData |  |
| 1042 | *Ordinal Only* | `0x10E950` | 23,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `DllGetClassObject` | `0x1143F0` | 65 | UnwindData |  |
| 2504 | *Ordinal Only* | `0x184D20` | 75 | UnwindData |  |
| 2500 | *Ordinal Only* | `0x185680` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | `CreatePresentationFactory` | `0x185E30` | 116 | UnwindData |  |
