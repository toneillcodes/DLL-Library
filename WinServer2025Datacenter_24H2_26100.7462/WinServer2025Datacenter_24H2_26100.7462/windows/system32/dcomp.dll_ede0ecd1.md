# Binary Specification: dcomp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dcomp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ede0ecd1a8be2aa0100e91888f63d8e5d22901933e91730125b16911cedae022`
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
| 2503 | *Ordinal Only* | `0x2920` | 158 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x6D9D0` | 63 | UnwindData |  |
| 2002 | *Ordinal Only* | `0x6F0F0` | 134 | UnwindData |  |
| 1031 | *Ordinal Only* | `0x926A0` | 304 | UnwindData |  |
| 2501 | *Ordinal Only* | `0x963B0` | 252 | UnwindData |  |
| 2001 | *Ordinal Only* | `0xAE6E0` | 134 | UnwindData |  |
| 1024 | `DllCanUnloadNow` | `0xB7170` | 42 | UnwindData |  |
| 1025 | `DllGetActivationFactory` | `0xB71A0` | 45 | UnwindData |  |
| 1101 | `DCompositionGetStatistics` | `0xB8FD0` | 47 | UnwindData |  |
| 1029 | `DwmFlush` | `0xB9010` | 3,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `DwmpEnableDDASupport` | `0xB9010` | 3,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `DCompositionGetTargetStatistics` | `0xB9F70` | 37 | UnwindData |  |
| 2502 | *Ordinal Only* | `0xBC020` | 2,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `DCompositionCreateSurfaceHandle` | `0xBCB40` | 136 | UnwindData |  |
| 1040 | *Ordinal Only* | `0xBFCB0` | 35 | UnwindData |  |
| 1104 | `DCompositionWaitForCompositorClock` | `0xC1DF0` | 25,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | *Ordinal Only* | `0xC8150` | 231 | UnwindData |  |
| 1100 | `DCompositionGetFrameId` | `0xCE160` | 27 | UnwindData |  |
| 1103 | `DCompositionBoostCompositorClock` | `0xDA850` | 27 | UnwindData |  |
| 1038 | *Ordinal Only* | `0xDDD90` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `DCompositionCreateDevice3` | `0xDED30` | 12,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | *Ordinal Only* | `0xE1D00` | 108 | UnwindData |  |
| 1021 | `DCompositionCreateDevice2` | `0xE2830` | 12,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | *Ordinal Only* | `0xE5980` | 199 | UnwindData |  |
| 1020 | `DCompositionCreateDevice` | `0xEBF70` | 134,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `DwmEnableMMCSS` | `0x10CD40` | 27 | UnwindData |  |
| 1017 | `DCompositionAttachMouseDragToHwnd` | `0x10CD70` | 110 | UnwindData |  |
| 1018 | `DCompositionAttachMouseWheelToHwnd` | `0x10CDF0` | 110 | UnwindData |  |
| 2505 | *Ordinal Only* | `0x10CE70` | 27 | UnwindData |  |
| 2007 | *Ordinal Only* | `0x10CEA0` | 11,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | *Ordinal Only* | `0x10FB90` | 138 | UnwindData |  |
| 1042 | *Ordinal Only* | `0x111760` | 23,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `DllGetClassObject` | `0x117200` | 65 | UnwindData |  |
| 2504 | *Ordinal Only* | `0x186620` | 75 | UnwindData |  |
| 2500 | *Ordinal Only* | `0x186F80` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | `CreatePresentationFactory` | `0x187730` | 116 | UnwindData |  |
